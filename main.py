from tkinter import Tk, LabelFrame, Label, Entry, Button, END

from stories import (
    aDate,
    goodMorning,
    oneThing,
    suprise,
    inTheMuseum,
    theHoneymoon,
    theRedJacket,
    theTest,
    aLittleBitOfMoney,
    saturdayNight,
    whosSpeaking,
    theDanceClass,
    doYouNeedHelp,
    theGarden,
    aStrangeNoise,
    aVacationInRome,
    theNewMall,
    happyBirthday,
    thePerfectTrip,
    theTourist
)
from utilities import use_chrome, validate_num


def start():
    # Start webdriver and loop through story scripts
    driver = use_chrome()
    for story in master_list.values():
        valid_count = validate_num(story["entry"].get())
        for _ in range(valid_count):
            story["script"](driver)

    driver.close()


def close():
    root.destroy()


master_list = {
    "A Date": {"script": aDate.aDate},
    "Good Morning": {"script": goodMorning.goodMorning},
    "One Thing": {"script": oneThing.oneThing},
    "Suprise": {"script": suprise.suprise},
    "In The Museum": {"script": inTheMuseum.inTheMuseum},
    "The Honeymoon": {"script": theHoneymoon.theHoneymoon},
    "The Red Jacket": {"script": theRedJacket.theRedJacket},
    "The Test": {"script": theTest.theTest},
    "A Little Bit Of Money": {"script": aLittleBitOfMoney.aLittleBitOfMoney},
    "Saturday Night": {"script": saturdayNight.saturdayNight},
    "Who's Speaking": {"script": whosSpeaking.whosSpeaking},
    "The Dance Class": {"script": theDanceClass.theDanceClass},
    "Do You Need Help?": {"script": doYouNeedHelp.doYouNeedHelp},
    "The Garden": {"script": theGarden.theGarden},
    "A Strange Noise": {"script": aStrangeNoise.aStrangeNoise},
    "A Vacation In Rome": {"script": aVacationInRome.aVacationInRome},
    "The New Mall": {"script": theNewMall.theNewMall},
    "Happy Birthday": {"script": happyBirthday.happyBirthday},
    "The Perfect Trip": {"script": thePerfectTrip.thePerfectTrip},
    "The Tourist": {"script": theTourist.theTourist},
}


# Create window
root = Tk()
root.title("Duolingo Story Bot")
root.bind("<Return>", lambda x: start())

# Window Label
title_label = Label(text="Duolingo Story Bot", font="bold 15")
title_label.grid(row=0, column=0, columnspan=2, pady=10)

# Story frame
story_frame = LabelFrame(root, text="Choose a Story", padx=10, pady=10)
story_frame.grid(row=1, column=0, padx=15)

# Loop through stories and create labels and entries
for index, script in enumerate(master_list.items()):
    name, story = script
    col_row = 0 if index <= 9 else 2
    Label(story_frame, text=name, anchor="e", width=16).grid(
        row=index % 10, column=0 + col_row
    )
    story["entry"] = Entry(story_frame, width=3)
    story["entry"].grid(row=index % 10, column=1 + col_row, sticky="w")
    story["entry"].insert(END, 0)

# Start Button
start_button = Button(root, text="START", width=20, height=3, command=start)
start_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

# Close Button
close_button = Button(root, text="CLOSE", width=15, height=1, command=close)
close_button.grid(row=3, column=0, columnspan=2, pady=20)

root.mainloop()
