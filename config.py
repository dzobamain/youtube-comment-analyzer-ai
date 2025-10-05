# config.py

class AppConfig:
    def __init__(self):
        # Basic app information
        self.app_name = "YouTube Comment Analyzer AI"
        self.version = "1.0.0"
        self.author = "Volodymyr Dzoba"
        self.license = "MIT"
        self.repository = "https://github.com/volodymyrdzoba/youtube-comment-analyzer-ai"
        self.description = (
            "Local AI-powered tool for analyzing YouTube video comments. "
            "Uses GPT4All-compatible models (.gguf) running fully offline."
        )

        # Optional metadata
        self.keywords = [
            "YouTube", "comments", "AI", "GPT4All", "LLaMA", "local models", "analysis"
        ]
        self.python_version_required = ">=3.10"
        self.supported_platforms = ["macOS", "Linux", "Windows"]

app_config = AppConfig()
