from crawlerWade52.tasks_crawler_finmind import crawler_finmind

# 發送到 twse 的 queue
task_2330 = crawler_finmind.s(stock_id="2330")
task_2330.apply_async(queue="twse")  # 發送任務
print("send task_2330 task")
# 發送到 tpex 的 queue
task_00679b = crawler_finmind.s(stock_id="00679B")  # 美債
task_00679b.apply_async(queue="tpex")  # 發送任務
print("send task_00679b task")
