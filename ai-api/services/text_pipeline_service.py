from services.text_stage1_service import run_stage1_kb_check
# from text_stage2_service import run_stage2_web_check
# from text_stage3_service import finalize_stage3

def process_fake_news_pipeline(query, collection, transformer, nli):

    # ===== STAGE 1 =====
    s1 = run_stage1_kb_check(collection, transformer, nli, query)
    return s1

    # if s1["is_stop"]:
    #     return finalize_stage3(query, s1, stage=1)

    # # ===== STAGE 2 =====
    # s2 = run_stage2_web_check(query, transformer, nli)

    # if s2["is_stop"]:
    #     return finalize_stage3(query, s2, stage=2)

    # # ===== STAGE 3 =====
    # return finalize_stage3(query, s2, stage=3)