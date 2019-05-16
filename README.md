# Twitter Sentiment Analysis
A Python script that analyses sentiment on a given topic from tweets data provided by Twitter

</br>

## Getting Started

The project requires authentication via the Twitter API. A new application needs to be created to get the necessary keys. A few libraries also need to be installed for the script to run properly.

### Prerequisites

* [Tweepy](http://www.tweepy.org), the official Python library for accessing the Twitter API
* [TextBlob](https://textblob.readthedocs.io/en/dev/), a Python library for processing textual data
* [NLTK](https://www.nltk.org) dataset, to help better natural language processing
* Keys from the [Twitter Developer Application Management](https://apps.twitter.com/) site
  - Consumer key
  - Consumer secret
  - Access token
  - Access token secret
  
### Installing

The **Tweepy** library can be installed by using the command
```
pip3 install tweepy
```  
</br>

The **TextBlob** library can be installed using
```
pip3 install textblob
```  
</br>

The **NLTK corpora** can be downloaded by using the following command
```
python3 -m textblob.download_corpora
```
These files will provide better natural language processing capabilites for the TextBlob library. 

> **Note:** A missing cerificate error can arise when trying to download the NLTK corpus files. To fix the issue, navigate to the Python folder `/Applications/Python 3.6` and run the `Install Certificates.command` file.

</br>

To obtain the **consumer keys** and **access tokens** from the Twitter Dev Application Management site, a new app needs to be created using a Twitter account.

* Open [apps.twitter.com](https://apps.twitter.com/) and use the `Create New App` button.
* Complete the form with the necessary application details. The application name must be unique.
* Navitgate to the `Keys and Access Tokens` tab.
* Copy `Consumer Key`, `Consumer Secret`, `Access Token` and `Access Token Secret` and update the variables `consumer_key`, `consumer_secret`, `access_token`, and `access_token_secret` in the `sentiment_analysis.py` file accordingly.

</br>

## Running the program

* Download the `sentimental_analysis.py` file from the repository
* Update the consumer keys and access token values with the appropriate data in the file
* Run the file using
```
python3 sentimental_analysis.py
```

</br>

## Sample output
```
(twitter_sentimental_analysis) ➜  twitter_sentimental_analysis git:(master) ✗ python sentimental_analysis.py

Enter Keyword/Tag to search about: modi
Enter how many tweets to search: 50   
RT @squintneon: The guy who made fun of Modi interview with Akshay &amp; shared by many Librats including @scroll_in is also saying "Aayega to…
RT @narendramodi: Kashmir to Kanyakumari, Jamnagar to Silchar…you would enjoy reading this article on the extent and diversity of my travel…
RT @BJP4India: PM Modi addresses public meeting in Pratapgarh, UP. Dial 9345014501 to listen LIVE. #DeshKiPasandModi https://t.co/Z3u3ZFVsCN
RT @SudheenKulkarni: When a leader's performance is poor, he seeks to divert people's attention.

Is #Modi talking about...

Education, Emp…
RT @Swamy39: My Professorial grades for Modi Sarkar: National  Security —A; Fighting corruption—B+; Macro economic development —C
@varinder_bansal As per pappu @RahulGandhi India has come at the bottom of list
RT @Joydas: This is the best Non Political questions to Narendra Modi. Simply superb https://t.co/KO4J3bWFa7
RT @kavita_krishnan: Modi darbari actor @akshaykumar claims he was given 'honorary citizenship of Canada'. But a 2012 report in a Canadian…
RT @SreenivasanJain: As controversy mounts over the spate of clean chits given by the EC to Modi-Shah, turns out in at least 5 cases, one o…
RT @GauravPandhi: Out of 6 Surgical Strikes during UPA's tenure, one was under @Gen_VKSingh as the COAS (30/8 - 1/9, 2011), one u/d Gen Dee…
RT @KrishnaPooniaIN: Army is not personal property of Modi. When Modiji questions Surgical Strikes, he insults Indian Army -@RahulGandhi

#…
RT @GauravPandhi: Out of 6 Surgical Strikes during UPA's tenure, one was under @Gen_VKSingh as the COAS (30/8 - 1/9, 2011), one u/d Gen Dee…
RT @JhaSanjay: By calling past surgical strikes as video games, #Modi has contemptuously dismissed the risks and courageous conduct of our…
RT @Swamy39: My Professorial grades for Modi Sarkar: National  Security —A; Fighting corruption—B+; Macro economic development —C
RT @report_real: #Modi has insulted Army by terming surgical strikes during Congress Govt as video games: @RahulGandhi
#ArmySeMaafiMaangoMo…
RT @waglenikhil: BJP is filled with rotten minded thugs who spread hatred at every second. This is the real anti-India brigade led by Modi…
RT @waglenikhil: BJP is filled with rotten minded thugs who spread hatred at every second. This is the real anti-India brigade led by Modi…
RT @RifatJawaid: Compare this interview with a series of interviews recently conducted by our 'intrepid' journalists of PM Modi. Can you no…
Under Modi government development for all without discrimination on caste, religion, region: Naqvi https://t.co/1cYFtZyyX9
Every man is N_arendra Modi before marriage and Man_mohan Singh after marriage!
RT @nupur11: World relates @narendramodi as 'Visionary'
Indians relates with 'Development'
Bhakts relates with him as 'Patriotic'
But this…
@sardesairajdeep @priyankagandhi @IndiaToday @aajtak Looking at Modi s support of all the people@ of Beneras she ra… https://t.co/xEKPFUlBdf
- Modi has let a terror-accused who says she started the demolition of Babri Masjid as a 4 yr Old &amp; is proud of it… https://t.co/tQCNlD6pxk
Modi Sir, my request is that now please try to ignore this baseless, cheat, liar family. This family does not befit… https://t.co/XuSuaIRAK1
RT @India_Policy: So @rajchengappa, in his interview of @RahulGandhi claimed that Modi promised to credit 15 lakh rupees in every Indian's…
RT @haripaltungar: Modi government adverse result are that That Indian Media  freedom is in danger .
     Exposed moadi and his slave Media…
RT @rssurjewala: Army is not a personal property of Mr. Modi. Surgical Strikes are done by the Armed Forces. When Mr. Modi says Surgical st…
RT @BJP4India: PM Modi addresses public meeting at Valmiki Nagar, Bihar. Dial 9345014501 to listen LIVE. #DeshKiPasandModi https://t.co/zD6…
RT @ ( narendramodi ) -

Addressing a large rally in Ramnagar, Bihar. Watch. https://t.co/A8R11hZr8k

— Chowkidar N… https://t.co/g0vLEGo9TL
RT @swapan55: I don’t think anything will be served by getting shirty over The Economist editorial. It has been written with inputs from In…
@ashoswai @ndtv India unfortunately under modi's regime has become Hindu extremist State,where minorities are suppr… https://t.co/yTuXTebCAV
RT @BJP4India: PM Modi addresses public meeting at Valmiki Nagar, Bihar. Dial 9345014501 to listen LIVE. #DeshKiPasandModi https://t.co/zD6…
RT @Anjali_Guptaa: At front of defence modi jee deal world class jet fighter and best air defence system S-400 Shows his commitment, After…
RT @KoomarShah: Modi insulted Soniaji as "Jersey Cow"

Modi insulted Rahulji as "Gaay ka Bachda"

Modi insulted Sunanda Pushkar as "50 cr G…
@kunalkamra88 But Aayga sirf Modi
RT @ashoswai: India Prime Minister Modi mocks 'Me Too' movement - Not unexpected from this foul-mouthed bigot who has deserted his wife and…
RT @GauravPandhi: Watch this press conference by @RahulGandhi ...he just tore into PM Modi plucking out a thread after thread. Terrific!

I…
RT @True_Human_: Hindu Muslim India Pakistan Vande Mataram BMKJ #AntiNational Masood Azhar Balakot etc etc are ONLY Agenda of BJP to polari…
RT @bainjal: The Modi era will be defined as the era of fakes &amp; frauds. Fake degrees, fake achievements &amp; now his prime time warrior who te…
RT @GauravPandhi: Watch this press conference by @RahulGandhi ...he just tore into PM Modi plucking out a thread after thread. Terrific!

I…
RT @INCIndia: As a nation under Modi we must always remember, "fear is the path to the dark side. Fear leads to anger. Anger leads to hate.…
RT @news18dotcom: .@narendramodi also said the @INCIndia has been reduced to the status of 'vote katwa' party and it will soon witness its…
RT @BJP4India: PM Modi addresses public meeting at Valmiki Nagar, Bihar. Dial 9345014501 to listen LIVE. #DeshKiPasandModi https://t.co/zD6…
RT @ANINewsUP: Amit Shah in Amethi: For the 1st time Amethi is feeling that development is possible here as well. Even after making members…
RT @arunjaitley: Yesterday, Rahul Gandhi said, “I have dismantled Modi’s image”, how do you damage the image of a person who is riding perh…
A man lacking wisdom and decency   statesman ship  is an alien word for this illiterate moron.. For Sure.. Shameful https://t.co/QSS7o8G7Sx
RT @KrishnaPooniaIN: Army is not personal property of Modi. When Modiji questions Surgical Strikes, he insults Indian Army -@RahulGandhi

#…
RT @INCKarnataka: Yes, as claimed by @BJP4India Modi has achieved so many firsts.

1st PM to spend more days in foreign land than in Indian…
@Actor_Siddharth @realDonaldTrump Good that Modi ji came to power in 2014. Getting to witness Bharath's Kalank(s) l… https://t.co/PMU6NtRAZz
RT @JhaSanjay: #Modi ‘s legacy: 
1) Lynching culture 
2) Demonetisation 
3) Pragya Singh Thakur 
4) Kabristan-Shamshan politics
5) Destroye…


Output:     
How people are reacting on modi by analyzing 50 tweets.

General Report: 
Positive

Detailed Report: 
34.00% people thought it was positive
16.00% people thought it was negative
50.00% people thought it was neutral
(twitter_sentimental_analysis) ➜  twitter_sentimental_analysis git:(master) ✗ 

  
```

</br>

## Authors

* **Neeraj Kumar Singh** - *Initial work* - [neeraj1909](https://github.com/neeraj1909)


See also the list of [contributors](https://github.com/neeraj1909/twitter_sentimental_analysis/graphs/contributors) who participated in this project.

</br>

## Acknowledgments

* [NLTK documentation](https://www.nltk.org)
* [TextBlob documentations](https://textblob.readthedocs.io/en/dev/quickstart.html#sentiment-analysis)
* [Twitter Sentiment Analysis - Learn Python for Data Science](https://www.youtube.com/watch?v=o_OZdbCzHUA)
* [Twitter Sentiment Analysis using Python](https://www.geeksforgeeks.org/twitter-sentiment-analysis-using-python/)












  