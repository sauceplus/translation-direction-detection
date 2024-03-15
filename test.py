import src.translation_direction_detection as tdd

detector = tdd.TranslationDirectionDetector()

sentence1 = "Können Sie mir dabei weiter helfen?"
sentence2 = "Pouvez-vous m'aider ?"
lang1 = "de"
lang2 = "fr"

result = detector.detect(sentence1, sentence2, lang1, lang2)
print(result)
# Predicted direction: de→fr
# 1 sentence pair
# de→fr: 0.554
# fr→de: 0.446