from urbans.urbans import Translator
# import pandas as pd
# import nltk
# nltk.download('punkt')
# from nltk.tokenize import word_tokenize


# df = pd.read_csv('News-Commentary_v16-sample-10.csv')


src_sentences = ["I love good dogs", "I hate bad dogs", 'They make perfect steaks', 'They make a cute couple']
# src_sentences = df.en.array()
# Source grammar in nltk parsing style
src_grammar = """
                S -> NP VP
                NP -> PRP
                VP -> VB NP
                NP -> JJ NN
                NP -> ART NP
                PRP -> 'I' | 'They'
                VB -> 'love' | 'hate' | 'make'
                JJ -> 'good' | 'bad' | 'perfect' | 'cute'
                NN -> 'dogs' | 'steaks' | 'couple'
                ART -> 'a'
                """

# Some edit within source grammar to target grammar
src_to_target_grammar =  {'CLS: NN tmp VB NN -> CLS: VB NN NN'}

# Word-by-word dictionary from source language to target language
en_to_zh_dict = {'I': '我', 'love': '愛', 'good': '好', 'dogs': '狗', 'hate': '討厭', 'bad': '壞', 'They': '他們', 'make': '做', 'perfect': '完美的', 'steaks': '牛排', 'a': '一', 'cute': '可愛的', 'couple': '情侶'}

translator = Translator(src_grammar = src_grammar,
                        src_to_tgt_grammar=src_to_target_grammar, 
                        src_to_tgt_dictionary = en_to_zh_dict)

trans_sentences = translator.translate(src_sentences) 
for t in zip(src_sentences, trans_sentences):
    print(t)