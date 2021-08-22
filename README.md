```
A
Project Synopsis On
```
##### “ Profanity Filter ”


```
By
Ms. MRUNMAYI PADWAL
Ms. BHAGYASHREE PATHAK
Ms. MRUGAKSHI THAKARE
Mr. DIVYESH VISHWAKARMA
```
```
Under the guidance of
```
###### Prof. Aruna Kamble

##### ACKNOWLEDGEMENT

The project “Profanity Filter” is creative work of many minds. A proper
synchronization between individual is must for any project to be completed
successfully. One cannot imagine the power of the force that guides us all and
neither can we succeed without acknowledging it.
We would like to express our gratitude to Principal Dr. Sandhya Jadhav and Dr.
D.R. Ignle , our Head of the department, Computer Engineering for encouraging
and inspiring us to carry out the project in the department lab. We would also
like to thank our Guide Prof. Aruna Kamble, Department of the Computer
Engineering for her expert guidance, encouragement and valuable suggestions
at every step.
We also would like to thank all the staff members Department of the Computer
Engineering for providing us with the required facilities and support towards the
completion of the project.
Last but not the least we are thankful to our parents and friends for their
constant Inspiration, encouragement and well wishes by which we have made a
challenging project.


##### TABLE OF CONTENTS

SR.NO
CHAPTER

```
1.
Introduction
1.1 Background Study 8
1.2 Problem Statement 10
```
```
2.
Aim and Objectives
```
```
3.
Architecture
13
```
```
4.
Tools and Techniques
```
```
5.
Algorithms
```
```
6.
Future Scope
```
```
7.
Conclusion
```
```
8.
References
```

# CHAPTER 1

# INTRODUCTION


##### 1. INTRODUCTION

In the context of this work we define profanity, curse, swear or taboo words, as
words used with offensive or vulgar intentions. Although swearing can be studied
in the context of multiple disciplines, from the computational perspective, it is
commonly associated with the automatic identification of abusive comments.
Most often the intent of profanity identification lays on censoring these words
or posts, but profanity is also tightly related with sentiment analysis and opinion
mining tasks , since it can adequately express certain emotions, mostly
negative. Its use seems to depend on several factors, such as gender, age and
social class.
How common is cursing on-line? Most pages of 16 year olds on MySpace, and
about 15% of pages of middle-aged people contained strong swearing. 9.28%
of comments in Yahoo! Buzz showed profanity. Out of 51 million tweets
in English, at least 7.73% of messages contained cursing , where swear words
represented 1.15% of all words seen — as frequent as first person plural pronouns
(we, us, our).

While profanity is a common occurrence on-line, correct spelling is not. Curse
words are not always written in the same way, a consequence of their use and
spread being more oral than written. Graphical diversity is also augmented by ac-
cidental misspellings or intended obfuscations.

Negative content can be problematic for sites wanting to expand their user base,
engage existing users, and foster a positive and collaborative community. Social
contracts and normative behaviors, however, are unique to specific socio-technical
systems. What is considered inappropriate in a given context is both site and
community specific. On many sites, community managers are primarily responsible
for the task of removing inappropriate content. However, the flood of user-generated
content on many sites quickly overwhelms community managers’ ability to
effectively manage it.


1.1 Background Study :

As more and more of the web has grown to include user-generated content, the
detection and management of inappropriate or objectionable content has
become an important task for web sites. One common technique is social
moderation, in which users themselves undertake the task of identifying and
flagging of profane or inappropriate responses. However these systems have
been only moderately successful, and suffer from potential collusion - flagging
can be used to indicate disagreement or dislike of a post that is not otherwise
inappropriate or profane. Instead of relying on social moderation, recent
proposals have been made to automate the detection of inappropriate or
abusive content.

Research in computer vision has given much attention to the related issue of
detecting inappropriate videos and images. Advances in this space have
largely included systems that detect “too much skin” in images and videos.
Other systems utilize textual metadata, while some combine the two; one such
system, WebGuard has reached 97.4% accuracy in detecting pornographic
web sites.

While many would argue that textual analysis is more tractable than visual
content analysis, this may be in part because of a general misunderstanding
about how difficult the problem of profanity detection is in real-world
contexts. Furthermore, text has a visual element that is socially understood.
Expressive forms such as emoticons and “ASCII art” use visual properties of
text, punctuation marks and symbols to mimic lexical units and thus convey
meaning, denote profanity and circumvent automatic filters. Such visual-for-
textual substitution is best illustrated through examples such as the use of “@”
in “@ss”.

Because of these misunderstandings, perhaps, comparatively little research has
focused on detecting inappropriate text in user-generated content systems. As
mentioned above, two groups have built systems to detect insults and
harassment in online forums and another has focused on cyberbullying of
teens, but even fewer have addressed the identification of profanity. Yoon et
al. built a system to detect newly coined profanities in Korean, in an attempt to
improve upon the failure of list-based systems to evolve along with profane
language. Due to the target audience being children, some have analyzed the
content of video game web sites and video games themselves to verify that
presented content meets ratings standards. However, work in this area does not
generally strive for automated analysis. Advancing our ability to detect and
remove profanity could have several significant, positive social consequences.
The growth of collaborative information products such as Wikipedia, Yahoo!


Answers, and Stack Overflow rely on the provision of interaction
environments that are supportive, productive, and meet the specific needs of
their user communities. Open-source software projects also rely on email lists
and forums to support the necessary community building, coordination, and
decision-making processes.

No automated system, by itself, can appropriately filter and manage ongoing
discourse and interaction so that it meets the needs of a particular topic,
domain, or user community. Indeed, research has illustrated the important role
of established community members for implicitly and explicitly
communicating language norms to new members. The enforcement of these
norms is often ad hoc, however. In large systems, the sheer volume of content
means ad hoc strategies often leave a large amount of profane or inappropriate
user-generated content undetected. The existence of such content can actually
fight against the positive influence of community managers and long-time
participants by setting a bad precedent that communicates to new users that
profanity and other negative content is acceptable [21]. Automated systems
that help community managers, moderators, and administrators to manage the
flood of user-generated content in these environments could help to promote
more productive large-scale collaboration and thus more valuable information
products.


1.2 Problem Statement :

1. TEXT
A profanity search and replace method. Returns the number of profane words
found and the submitted text with profane words replaced with symbol
provided. If the text is clean 0 (zero) is returned.

Arguments:
api_key (Required)
Your API application key.

text (Required)
The text you want checked for profanity.

replacesymbol (Required)
The symbol you want to replace each letter of the profane word with.

2. IMAGE
Our solution can be used to moderate or filter any web-hosted photo including
avatars, profile pictures, contest entries, photo album pics, etc.

By submitting the URL of the image, which consists of profane text, we return
the same image by blurring / by replacing the text in the image which contains
profane text by symbols.


# CHAPTER 2

# AIM & OBJECTIVE


##### 2. AIM & OBJECTIVE

###### Aim

To filter out profane, obscene and other unwanted content.

###### Objective

As user-generated Web content increases, the amount of inappropriate and/or objectionable
content also grows. Several scholarly communities are addressing how to detect and manage
such content: research in computer vision focuses on detection of inappropriate images,
natural language processing technology has advanced to recognize insults. However,
profanity detection systems remain flawed. Current list-based profanity detection systems
have two limitations. First, they are easy to circumvent and easily become stale–that is, they
cannot adapt to misspellings, abbreviations, and the fast pace of profane slang evolution.
Secondly, they offer a one-size fits all solution; they typically do not accommodate domain,
community and context specific needs. However, social settings have their own normative
behaviors–what is deemed acceptable in one community may not be in another. In this paper,
through analysis of comments from a social news site, we provide evidence that current
systems are performing poorly and evaluate the cases on which they fail. We then address
community differences regarding creation/tolerance of profanity and suggest a shift to more
contextually nuanced profanity detection systems.


# CHAPTER 3

# ARCHITECTURE


##### 3. ARCHITECTURE

The model schema explains the basic architecture of the project. The
architecture consists of 3 sections namely:

1. Profanity Text Filter Model Schema
2. Profane Image Filter Model Schema
3. API Model Schema

Let's discuss them in detail.

1. Profanity Text Filter Model Schema:

The model schema consists of the root called as the ProfaneList.
The profane list has 3 sub divisions:
a. Profane words
b. Date Created
c. Date Edited
Profane words when added newly to the database, first they are checked
that they are unique or not( non case sensitive). If they are unique then they are
automatically assigned date of Creation and Date of editing as the system date.


2. Profane Image Filter Model Schema:

The model schema for image consists of ProfaneImage as root.

The ProfaneImage has 3 sub divisions:

a. Image Input
b. Image Output
c. Date Edited
Similar to ext profanity filter model shema, this section takes one Input
Image and produces output. This model schema indirectly inherits from text
model schema. The date edited is the date of creation of the output image.


3. API Model Schema:

The API model schema consists of 2 things of which the root node is API
namely

a. Request
b. Response
c. Status
The request section keeps an account of the request that the api got from
the user.

The Response keeps an account of the response that has to be sent to the
user

The status represents the status of the request sent by the user

System Structure:

One can use the api to get results for the following things:

a. To filter just text
b. To filter just images
c. To filter both
Thus the system categorises requests in the following manner:


1. First The system identifies the type of request and categorises them as for
    images or for text or both. If the request type is valid the system returns a
    status response of 200 and proceeds to the next request or response cycle.
2. If the request is not of any of the above type then it returns either with
    404 , or no- response.


## CHAPTER 4

## TOOLS AND TECHNIQUES:


##### 4. TOOLS AND TECHNIQUES:

###### Tools:

Here’s a list of all the software tools used in the making of this project.

1. Python: Python is an interpreted high-level general-purpose programming
    language. Python's design philosophy emphasizes code readability with
    its notable use of significant indentation.
2. Django: Django is a Python-based free and open-source web framework
    that follows the model-template-views architectural pattern.
3. Niepage: Nicepage is a website builder software breaking limitations
    common for website builders with revolutionary freehand positioning.
    7000+ Free Templates
4. Bootstrap: Bootstrap is a free and open-source CSS framework directed at
    responsive, mobile-first front-end web development. It contains CSS- and
    JavaScript-based design templates for typography, forms, buttons,
    navigation, and other interface components.
5. Google Vision API: Derives Insights From Images With Google's
    Powerful Cloud Vision API.It has Innovative Machine Learning Products
    & Services for Developers & Data Scientists.
6. Pillow: Python Imaging Library is a free and open-source additional
    library for the Python programming language that adds support for
    opening, manipulating, and saving many different image file formats.
7. Heroku: Heroku is a cloud platform as a service supporting several
    programming languages. One of the first cloud platforms, Heroku has
    been in development since June 2007, when it supported only the Ruby
    programming language, but now supports Java, Node.js, Scala, Clojure,
    Python, PHP, and Go.
8. RapidAPI: RapidAPI's Enterprise Hub is an internal API Marketplace
    that is customized to match any company's brand, integrates seamlessly
    with internal systems.
9. LucidChart: Lucidchart is a web-based proprietary platform that allows
    users to collaborate on drawing, revising and sharing charts and diagrams.
10. Github: GitHub, Inc. is a provider of Internet hosting for software
    development and version control using Git. It offers the distributed


```
version control and source code management functionality of Git, plus its
own features.
```
###### Techniques:

There are several sub processes going on in the system altogether. So here are
the following significant processes that are running in the project’s system.

1. Filtering Profane Words From Text
2. Detecting and Blurring Profane words from an image
3. API request response handling.
Here is the detailed description and methodology of the process that are going
on.
1. Filtering Profane Words From Text:
Here’s the technique:
Explanation:
a. Initially all the profane words present in the database are imported
onto the views.py (the html response handling file)
b. Then the page loads and displays every element.
c. The page has an input field i the profanity text filter section of the
html page, which takes the input from the user.
d. Once the user inputs the data and clicks Check Profanity, then the
input data is read by the form fields named content and gets stored
in a variable.
e. Now the variable is converted into a list using the python method
“split()”
f. That list is then iterated over word to word. Then it categorises the
words as following types.
i. Only Alphanumeric Words
ii. Words with special symbol
g. Now it iterates over every alphanumeric word and checks if that
particular word is present in the database or not. If that word is in
the database then it is converted into stars and that starred word
replies the real word in the list at that same index. If the word is not
in the database then it's simply passed over and nothing is done to
that word.


```
h. If the word has some special symbols then that word is iterated
over each letter and checked if it makes a meaningful word or not,
if that word is present in the database then it is starred, else it is
passed and done with no changes at the exact same index.
i. The final list is then joined with spaces using the ‘.join()’ method.
And sent to the output field named context. The output then is
displayed to the user in the results box of text profanity.
```
2. Detecting and Blurring Profane words from an image:

Here’s the algorithm:

Explanation:

```
a. Initially the views.py loads the respective html page on the
browser.
b. In the image section of the webpage, the user needs to inputs
an image.
c. That imagefile is loaded onto the input field named filein
d. Then that image is loaded onto the google Vision Api
handler.
e. The vision api initially checks for the proper google
credentials and the api key.
f. If both the credentials and the api key is proper then an
image request is sent to google and a response is awaited,.
g. As soon as we get a positive response, we send a text
annotation request to google.
h. As we get the text annotation positive response, we store the
response in a variable same that was done in text profanity
filter
i. Then the Text profanity filter process runs. But instead of
staring out the word, we then generate a request to get the
coordinates of that word to google.
j. When we get the vertices of that word we crop that part of
the image.
k. Then we take the top left diagonal coordinate and bottom
right coordinate and pass it for the next process
```

```
l. When the diagonal vertices are passed to the pillow
library,then using the Gausian blur technique with a very
high radius, we blur that section of the image.
m. The final blurred section is then pasted on the initially
cropped image and the final output image is produced.(
Django keeps a track of dynamic nomenclature of the output
image file using the system date and time to name the output
image - So that every image has a unique name to avoid
overwriting)
n. Then the final image is passed out to the out-file variable and
displayed to the user as context of the webpage.
```
3. API request response handling.

This section handles all the requests among users, google and the
main server of the api. It also sends status reports.


# CHAPTER 5

# ALGORITHMS


##### 5. ALGORITHMS

###### TEXT FILTER:

1. Input a string from user
2. Store all the words of the string in a list
3. Make the words case-insensitive
4. Check if the word from the list is present in the database or not
5. If present, replace the characters of the word by “*”
6. Repeat step 4 until all the words from the list are checked
7. If the word is not present in the list, check if the word contains a special
    character or not
8. If it does, create a string variable “thatword’, and add all the characters
    (excluding special characters to the thatword).
9. If the value of thatword is present in the word and it is present in the
    database , then replace the letters of the word by “*”.
10 .Repeat the step 7,until all the words from the list are checked.
11. Join all the elements of the list into a string and return it

###### IMAGE FILTER:

1. Choose the Image to Upload
2. Read the image using Google cloud vision API
3. Request for TEXT_DETECTION for extracting the text
4. Store text annotations in a variable text
5. Convert the text into a list
6. Store the index of the profane word from the list in variable c
7. Using the index find the vertices of the bounding polygon of the profane
    word
8. Store the top-right x and y vertices and bottom-left x and y vertices of the
    bounding polygon in variables a1,a2,b1,b2 respectively
9. Using Pillow library, crop the image by passing the vertices a1,a2,b1,b2
10. Blur the cropped image
11. Paste the blurred image on the original image
12. Return the original image


# CHAPTER 6

# FUTURE SCOPE


##### 6. FUTURE SCOPE:

Following the conclusions drawn in this article, there are a few clear next steps with regard to
moving beyond listbased profanity detection systems, and tailoring systems for specific
communities.

First, since list-based profanity detection systems don’t suffice, future work involves building
profanity detection systems from a machine learning point of view that take into account the
context in which profane language is used. Learning the context, in addition to the actual
profane words, has a greater potential for robustness, enabling the system to stand up to
misspellings, disguised or partially censored words and evolving profane language. Similarly
relevance feedback can be used to adapt and improve the model over time.

Secondly, since we established that profanity use and tolerance is very specific to a
community, it is very clear that these systems will have to be developed or trained by each
community. Future work involves building toolkits that allow this sort of tailoring. The use of
Amazon Mechanical Turk and other low cost crowdsourcing mechanisms will prove crucial
in labeling profanity in data sets from each community in order to train these machine
learning systems.

Finally, we believe our results are most valuable as part of a larger investigation into the
social nature of profanity and negative content within specific domains and user
communities. In future studies we intend to extend our explorations of the social meanings of
profanity and its context-specific use through qualitative interviews and survey studies.
Furthermore, we expect that cross-site studies may be particularly revealing about the uses of
profanity and possible context-specific approaches for detecting it. In future work we hope to
compare and contrast multiple data sets that share a topical domain (e.g. politics) but are
drawn from several different sites.


# CHAPTER 7

# CONCLUSION


##### 7.CONCLUSION:

We had an aim to create a profanity filter API that will restrict the use of
profane words in texts or images for the user inputs. That will ultimately help us
to curb cyberbullying activities.

We used Python to create the backend of the project. And HTML, CSS,
Javascript for the front end.

With this project, we created an API to filter out profane, obscene and other
unwanted content. Hence, we achieved our aim successfully.


# CHAPTER 8

# REFERENCES

##### 8.REFERENCES:

➢ Profane Words List: https://www.cs.cmu.edu/~biglou/resources/
➢ Vision API Documentation: https://cloud.google.com/vision/docs

➢ Vision API Tutorials:
https://www.youtube.com/watch?v=xKvffLRSyPk&list=PL3JVwFmb_B
nSLFyVThMfEavAEZYHBpWEd

➢ Django Documentation: https://docs.djangoproject.com/en/3.2/


