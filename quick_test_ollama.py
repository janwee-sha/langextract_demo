import langextract as lx
import textwrap

# 1. 定义抽取规则（Prompt）
prompt = textwrap.dedent("""
Extract characters, emotions, and relationships in order of appearance.
Use exact text for extractions. Do not paraphrase or overlap entities.
Provide meaningful attributes for each entity.
""")

# 2. 给 AI 一个示例，告诉它“你想要什么结果”
examples = [
    lx.data.ExampleData(
        text="ROMEO. But soft! What light through yonder window breaks?",
        extractions=[
            lx.data.Extraction(
                extraction_class="character",
                extraction_text="ROMEO",
                attributes={"emotion": "wonder"}
            )
        ]
    )
]

# 3. 待处理文本
input_text = "Lady Juliet gazed longingly at the stars, her heart aching for Romeo"

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
    print(
        f"位置: {extraction.char_interval.start_pos}-"
        f"{extraction.char_interval.end_pos}"
    )
    print("----")