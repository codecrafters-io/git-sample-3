import random
import os
import shutil

random_words = [
	"humpty",
	"dumpty",
	"horsey",
	"donkey",
	"yikes",
	"monkey",
	"doo",
	"scooby",
	"dooby",
	"vanilla",
]

random.seed(2)

def words(count):
    def f():
        yielded = []
        while len(yielded) < count:
            chosen = random.choice(random_words)
            if chosen in yielded:
                next
            else:
                yielded.append(chosen)
                yield chosen

    return list(f())
    

def create():
    for word in random_words:
        shutil.rmtree(word, ignore_errors=True)

    folder_names = words(5)
    for folder_name in folder_names:
        print(f"- Creating {folder_name}")
        os.mkdir(folder_name)
        sub_folder_names = words(random.randint(0, 10))
        for sub_folder_name in sub_folder_names:
            print(f" - {sub_folder_name}")
            os.mkdir(f"{folder_name}/{sub_folder_name}")
            file_names = words(random.randint(0, 10))
            for file_name in file_names:
                print(f"   - {file_name}")
                f = open(f"{folder_name}/{sub_folder_name}/{file_name}", "w")
                contents = " ".join(words(random.randint(0, 10)))
                f.write(contents)
                f.close()
    

if __name__ == "__main__":
    create()
