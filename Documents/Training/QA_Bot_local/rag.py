from dotenv import load_dotenv
import os
from src.llm import LLM, EmbeddingModel
from src.document import Document, document_shibuya
from src.search import SimpleVectorSearch

# 環境変数の設定
# OpenAI以外のモデルを使用するときは適宜書き換える
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

## RAG研修で使用したコードをここに移植してください
class RAG:
    def __init__(self):
        self.llm = LLM(
            model_name="gpt-4o-mini",
        )
        self.embedder = EmbeddingModel(
            model_name="text-embedding-3-small",
        )
        self.searcher = SimpleVectorSearch(self.embedder)

    def add_documents(self, documents: list[Document]):
        """検索システムに文書を追加する"""
        self.searcher.add_documents(documents)

    def use_llm(self, prompt: str) -> str:
        """LLMと通信する"""
        return self.llm.completion(prompt)

    def create_prompt_for_search(self, user_query: str) -> str:
        """
        ユーザーのクエリから、検索クエリ生成用のプロンプトを生成する。
        プロンプトを作るだけ。
        """
        search_prompt = f"検索クエリ: {user_query}\nユーザの質問に答えるために関連する文書を検索してください"

        return search_prompt
    

    def search(self, query: str) -> list[Document]:
        """検索を行う"""
        return self.searcher.search(query, k=3)
    

    def create_prompt_for_answer(self, user_query: str, documents: list[Document]) -> str:
        """検索結果をLLMに渡し、回答を生成するためのプロンプトを生成する"""
        # プロンプトのイメージ
        #
        # ＜元の質問+LLMへの指示1 (質問と検索結果の提示)＞
        #
        # ＜文書1＞
        # ------
        # ＜文書2＞
        # ------
        # ....
        # ------
        # ＜文書N＞
        # 
        # ＜LLMへの指示2 (回答を生成せよ)＞
        documents_content = "\n\n".join([f"ドキュメント {i + 1}:\n{doc.text}" for i, doc in enumerate(documents)])
        
        answer_prompt = f"ユーザの質問; {user_query}\n以下の検索結果を参考にして, 質問に対する最適な回答を生成してください. 参考文書に記載されていない内容は使用せず, 分からない場合はその旨を述べてください \n\n{documents_content}\n\n回答を生成してください"
        
        return answer_prompt
    

    
    def answer(self, user_query: str) -> str:
        """
        RAGを実施する
        """
        ### クエリの生成
        prompt_for_search = self.create_prompt_for_search(user_query)
        llm_response = self.use_llm(prompt_for_search)
    
        ### llm_responseに適切な処理を行い、queryを取り出す
        query = llm_response

        ### 検索
        documents = self.search(query)

        ### 回答の生成
        prompt_for_answer = self.create_prompt_for_answer(user_query, documents)
        llm_response = self.use_llm(prompt_for_answer)       

        ### llm_responseに適切な処理を行い、answerを取り出す
        answer = llm_response 

        return answer
    
if __name__ == '__main__':
    rag = RAG()
    rag.add_documents(document_shibuya())
    rag.searcher.save()

    # rag.searcher.load()
    # print(rag.answer("渋谷区の基本計画について教えてください。"))
