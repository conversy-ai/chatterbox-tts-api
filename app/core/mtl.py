'''
Multilingual support for the tts model

This is a temporary file to support the multilingual model.
It will be removed when the multilingual model is fully supported.

The SUPPORTED_LANGUAGES constant is overriden from the chatterbox.mtl_tts module to
reflect the languages that are supported.

Chinese was excluded because pkuseg would not install. The tokenizer asks for
spacy_pkuseg instead, and that is present and working in the image - it segments
"你需要在四月十五日之前提交一份医生证明。" correctly - so the exclusion outlived its reason
and Chinese is back.
'''

# Supported languages for the multilingual model
SUPPORTED_LANGUAGES = {
  "ar": "Arabic",
  "da": "Danish",
  "de": "German",
  "el": "Greek",
  "en": "English",
  "es": "Spanish",
  "fi": "Finnish",
  "fr": "French",
  "he": "Hebrew",
  "hi": "Hindi",
  "it": "Italian",
  "ja": "Japanese",
  "ko": "Korean",
  "ms": "Malay",
  "nl": "Dutch",
  "no": "Norwegian",
  "pl": "Polish",
  "pt": "Portuguese",
  "ru": "Russian",
  "sv": "Swedish",
  "sw": "Swahili",
  "tr": "Turkish",
  "zh": "Chinese",
}