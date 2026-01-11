## 什么是 LangExtract？

LangExtract 是一个基于大语言模型（如 OpenAI、Claude、Google AI 等）的 **信息抽取工具库**。  
它的核心能力是：

- 从**非结构化文本**中提取你关心的信息
- 支持**自定义实体类型**（不局限于“人名 / 地点 / 组织”）
- 支持为每个实体附加**上下文属性**

你可以把它理解为一个可以通过自然语言说明规则，让 AI 按你的业务需求‘读文本、做标注’的工具。

## 本地安装 Ollma 模型

Langextract 可以支持大部分LLM模型，本文使用本地 Ollama 模型来进行演示。

从 [Ollama 官网](https://ollama.com/) 下载并安装 Ollama。然后验证安装结果：

```bash
ollama --version
```

下载一个本地模型：

```bash
ollama pull qwen3
```

验证模型是否能运行：

```bash
ollama run qwen3
```
## 激活并使用Python虚拟环境（可选）

```bash
python -m venv langextract_env
source langextract_env/bin/activate  # On Windows: langextract_env\Scripts\activate
```

## 安装Langextract

```bash
pip install langextract
```
说明：

- `pip`：Python 的包管理工具

## 快速验证

```bash
python quick_test_ollama.py
```

示例结果:
```bash
LangExtract: Processing, current=53 chars, processed=0 chars:  [00:04]
Extraction successful!
类型: character
文本: 怪物
属性: {'alias': ['天蓬元帅']}
----
类型: action
文本: 调戏嫦娥
属性: {'actor': '怪物'}
----
类型: action
文本: 被打
属性: {'actor': '怪物', 'target': '玉帝'}
----
```
# 参考

# 参考
[Langextract](https://github.com/google/langextract)