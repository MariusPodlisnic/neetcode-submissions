class TextProcessor:
    # Implement method overloading for format_text method
    def format_text(self,text1:str,text2:str = "") -> str:
        result = ""
        if text2 == "":
            text1=text1.upper()
            return text1
        elif text1 and text2:
            result = text1+text2
        return result



# Don't modify the code below
processor = TextProcessor()
print(processor.format_text("hello"))
print(processor.format_text("hello", "world"))
