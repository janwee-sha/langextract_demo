import langextract as lx
import textwrap

# 1. 定义抽取规则（Prompt）
prompt = textwrap.dedent("""
从中文文本中抽取与《西游记》相关的关键信息。

请按文本出现顺序抽取以下实体：
1. 人物（character）
2. 人物的别名或称谓（alias）
3. 明确描述的行为（action）

要求：
- 抽取内容必须使用原文中的“原句或原词”，不要改写
- 不要合并不同实体
- 可为每个实体补充必要的属性来说明上下文
""")

# 2. 给 AI 一个示例，告诉它“你想要什么结果”
examples = [
    lx.data.ExampleData(
        text="行者道：“俺老孙乃齐天大圣孙悟空。”说罢，举起金箍棒便打。",
        extractions=[
            lx.data.Extraction(
                extraction_class="character",
                extraction_text="行者",
                attributes={"alias": ["齐天大圣", "孙悟空"]}
            ),
            lx.data.Extraction(
                extraction_class="action",
                extraction_text="举起金箍棒便打",
                attributes={"actor": "行者"}
            )
        ]
    )
]

# 3. 待处理文本
input_text = "怪物道：“我不是野豕，亦不是老彘，我本是天河里天蓬元帅。只因带酒调戏嫦娥，玉帝把我打了二千锤，贬下凡尘。”"

# 4. 执行抽取
result = lx.extract(
    text_or_documents=input_text,
    prompt_description=prompt,
    examples=examples,
    model_id="qwen3"
)

print("Extraction successful!")

# 5. 查看抽取结果
for extraction in result.extractions:
    print(f"类型: {extraction.extraction_class}")
    print(f"文本: {extraction.extraction_text}")
    print(f"属性: {extraction.attributes}")
    print("----")