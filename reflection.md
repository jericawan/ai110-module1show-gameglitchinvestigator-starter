# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  When I first opened the game, I did not see any visual errors, but during my first attempt I noticed that the attempts wouldn't change after the first guess was made. Another flaw I noticed is that once the first game is done, the new game button does not work, and to restart the game I must reload the page. 

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  23 |   "Go higher!"        "Go Lower!"       no error shown 
initial opening|Attempts left:8 Attempts left: 7  no error shown
| "hard" | range 1-100        range 1-50          no error shown

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
 I used claude for this project. 
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
I requested the AI to help with fixing the "new game" button on the UI. Orginially nothing would output when I clicked the button, this is due to an issue with the state changes within app.py. I found that the AI was able to help me reset these issues completely.
- Give one example of an AI suggestion you did not accept as written (including what the AI suggested, why you rejected or changed it, and how you verified your version). It does not have to be a suggestion that was wrong: over-engineered, out of scope, harder to read, or a poor fit for this codebase all count.
I pesonally didn't have any straight up rejections from the AI suggestions but I did find at times that it would write the FIXME comments for me and what was changed and I edited that to better reflect the changes made. 

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I would ask the AI to create the pytest then I would personally test the application myself to determine if the bug that I stated was fixed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  A manual test I did was during the first iteration of issues that I fixed, which would be the difficulty ranges. I went through the different difficulties to ensure that the ranges properly matched up (as it became more difficult, the ranges increased)
- Did AI help you design or understand any tests? How?
I do believe that AI did help me understand the tests because it would give a description of the created test and how it proves that the bug was solved. 
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
Streamlit is a source that allows a user to create a UI for an application without using HTML and CSS. 


---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  One strategy or habit from this project that I want to reuse for future labs/project is highlighting where I think the bug/issues occur. This allows me highlight errors especially when making specific requests for AI. 
- What is one thing you would do differently next time you work with AI on a coding task?
One thing I could have done differently when working with AI on a coding task and change the different options on the AI bot whether it is the model or the effort. 
- In one or two sentences, describe how this project changed the way you think about AI generated code.
I believe that this project changed the way i think about AI generated code as it allows mee to gain a better understanding on how bugs are changed and how word choice plays a big role in properly correcting code with AI. 
