import os
import random
from time import sleep

import streamlit as st

INTRO = ["ברוכים הבאים!",
         "אני התהילבוט ואני יודע הכל על תהילה",
         "סתם אני עדיין לומד עליה היא קצת מסובכת",
         "מקווה שמתישהו באמת אדע עליה הכל ואענה לכם על הכל",
         "בקיצור, חבר שלה הגבר הכין אותי",
         "אין עליו בעולם",
         "הוא גם חתיך אש",
         "יאללה בואו נתחיל"
         ]

QA_BANK = {
    "מה השם האמצעי של תהילה?": "בתיה :innocent:",
    "מה המושג היחיד שהיא יודעת מעולם ההייטק?": "ג'ייסון",
    "מי האדם שתהילה הכי אוהבת?": "באמת שאלתם את זה? ברור שאת מאור",
    "מה הסדרה האהובה על תהילה?": "The Office, תתאמצו יותר",
    "מי הדמות האהובה על תהילה?": "Dwight, you ignorant slut",
    "באיזה גיל תהילה עלתה לארץ שהיא חושבת שזה עדיין סביר להשתמש בזה כתירוץ כשהיא מעוותת מילים?": "8 :rage:",
    "מה תהילה שומעת כשמדברים אליה כשהיא בטלפון?": "כלום :weary: ",
    "מה תהילה הכי אוהבת בגופה?": "התחת שלה 	:peach:",
    "איפה תהילה ומאור הכירו?": """Mexico, 20°37'46.6"N 87°04'10.4"W""",
    "מי ישן עם תהילה כל לילה מחדש? (רמז - לא מאור)": "גדעון :llama:",
    "מי האויבת הגדולה ביותר של תהילה?": "תהילונת",
}
FAN_FACTS = [
    "תהילה טמבלית",
    "תהילה בחיים לא נשארה ערה כשראתה סרט עם מאור",
    "תהילה אכלה פעם 3 צלחות חומוס ברצף",
    "תהילה לא ראתה הפיג'מות",
    "תהילה תעשה הכל בשביל משחק 'מה הסיכויים'",
    "תהילה אוהבת להמציא מילים, ביניהם: סקוושווישים",
    "תהילה טוענת שהיא מתה על שומרי הגלקסיה אבל נרדמה בסרט האחרון",
    "3 דקות אחרי שתהילה נרדמת כל הגוף שלה קופץ. כל פעם."

]
SONGS = [
    "R U Mine? - Arctic monkeys",
    "why'd you only call me when you're high? - Arctic monkeys",
    "here come the sun - the beatles",
    "הבלדה למחלקה להלבשה תחתונה - מרסדס בנד",
    "עומר אדם - מים שקופים"
]


class Bot:
    def __init__(self):
        self.qa_bank = QA_BANK
        self.fun_facts = FAN_FACTS
        self.songs = SONGS

    def get_answer(self, question):
        return self.qa_bank.get(question, 'מצטער אין לי שמץ :smile:')

    def get_fun_fact(self):
        return random.choice(self.fun_facts)

    def get_song(self):
        return random.choice(self.songs)

    def get_the_highest_score(self, query):
        # returns the most similar question from the bank, if the similarity score is above 50%
        words_in_query = query.split(" ")
        highest_score = 0
        best_question = ""
        questions = self.qa_bank.keys()
        for question in questions:
            score = 0
            for word in words_in_query:
                if word in question:
                    score += 1
            if score > highest_score:
                highest_score = score
                best_question = question
        best_question_words = best_question.split(" ")
        if (len(best_question_words) / 2) > len(words_in_query):
            best_question = ""
        return best_question


# tab1:
@st.cache_data(show_spinner=False)
def intro_tab():
    for line in INTRO:
        st.write(line)
        sleep(1.5)


# tab 2:
def questions_tab(bot):
    questions = list(bot.qa_bank.keys())
    for q in questions:
        if st.button(q):
            answer = bot.get_answer(q)
            st.write(f'{answer}')
    question = st.text_input('שאלה חופשית')
    stored_question = bot.get_the_highest_score(question)
    if st.button('שאל אותי שאלה', key="free_question"):
        answer = bot.get_answer(stored_question)
        if question != stored_question and stored_question != "":
            st.write(f"נראה לי שהתכוונת לשאלה:", stored_question)
        st.write(f'{answer}')


# tab 3:
def pics_tab():
    directory = "tehilla_pics/"
    image_files = [f for f in os.listdir(directory)]
    if not image_files:
        st.warning("No images found.")
        return
    random.shuffle(image_files)
    for image_file in image_files:
        image_path = os.path.join(directory, image_file)
        st.image(image_path, caption=image_file, width=350)
        # todo: change pics names - affect the captions


# tab 4:
def get_random_pic():
    available_dirs = ["funny_pics/", "sleep_pics/", "tehilla_pics/"]
    directory = random.choice(available_dirs)
    image_files = [f for f in os.listdir(directory)]
    image_file = random.choice(image_files)
    image_path = os.path.join(directory, image_file)
    return image_path


def get_sleep_pic():
    directory = "sleep_pics/"
    image_files = [f for f in os.listdir(directory)]
    image_file = random.choice(image_files)
    image_path = os.path.join(directory, image_file)
    return image_path


def get_random_video():
    directory = "videos/"
    video_files = [f for f in os.listdir(directory)]
    random_video = random.choice(video_files)
    video_path = os.path.join(directory, random_video)
    video_file = open(video_path, 'rb')
    return video_file.read()


def make_button_key():
    return random.randint(1, 999)


def main():
    bot = Bot()
    st.title('התהילבוט')
    tab1, tab2, tab3, tab4 = st.tabs(["הקדמה", "שאל את המומחה", "תמונות של הטמבלית", "תלמדו על תהילה"])

    with tab1:
        intro_tab()

    with tab2:
        questions_tab(bot)

    with tab3:
        pics_tab()

    with tab4:
        if st.button(f":rainbow[תן לי עובדה מעניינת על תהילה]"):
            fun_fact = bot.get_fun_fact()
            st.write(f"הידעת? {fun_fact}")
            st.image(get_random_pic(), width=200)
        if st.button(f":rainbow[תן לי המלצה לשיר שתהילה אוהבת]"):
            song = bot.get_song()
            st.write(song)
            st.image(get_random_pic(), width=200)
        if st.button(f":rainbow[תן לי סרטון של תהילה]"):
            video = get_random_video()
            st.video(video)

        if st.button(f":rainbow[תן לי תמונה של תהילה ישנה]"):
            st.image(get_sleep_pic(), width=300)


if __name__ == '__main__':
    main()

# to see the pages-test option - rename the 'pages-test' to 'pages-test' and run streamlit run home.py
