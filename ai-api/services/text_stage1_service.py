from services.chroma_service import search_from_text
from services.nli_service import run_nli
from services.db_service import get_row_by_id

def run_stage1_kb_check(collection, transformer, nli, query, top_k=5, gap_threshold=5.0):

    results = search_from_text(collection, transformer, query, top_k=top_k)

    if not results:
        return {
            "top_k": top_k,
            "data": []
        }

    first_score = results[0]["score"]

    filtered = [
        r for r in results
        if abs(r["score"] - first_score) <= gap_threshold
    ]

    if not filtered:
        return {
            "top_k": top_k,
            "data": []
        }

    candidate_rows = [get_row_by_id(r["id"]) for r in filtered]

    pairs = [(query, row.get("judul", "")) for row in candidate_rows]

    nli_scores = run_nli(nli, pairs)

    enriched = []
    for r, nli_res, row in zip(filtered, nli_scores, candidate_rows):
        enriched.append({
            **r,
            "judul": row.get("judul"),
            "nli_label": nli_res["label"],
            "nli_score": nli_res["score"],
            "hoax_text": row.get("hoax_text"),
            "fakta": row.get("fakta"),
            "kategori": row.get("kategori"),
            "link": row.get("link"),
            "link_counter": row.get("link_counter"),
        })

    return {
        "top_k": top_k,
        "data": enriched
    }