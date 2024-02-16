# Customer Experience Analyzer with GenAI

![alt text](https://www.gosurvey.in/media/a0vmcbf1/customer-experience-is-important-for-businesses.jpg)

# Goal of Project

This data science project focuses on curating a thorough collection of issues reported by users of Payment Apps, centering on frequent challenges such as account management, transaction handling, and customer service, along with product, system, and feature malfunctions. It then delves into the emotional responses elicited by these challenges, analyzing sentiments expressed in user feedback, ranging from satisfaction and frustration to trust and dissatisfaction. By examining both the practical difficulties and the emotional reactions of Payment App users, specifically those using **PhonePe and Google Pay**, this project aims to offer an in-depth understanding of the overall user experience encountered on these platforms.
![alt text](https://cdn.timesbull.com/wp-content/uploads/2024/02/PhonePe-and-Google-Pay-jpg.webp)

> [!CAUTION]
> This content aims to illustrate the capabilities of NLP and Generative AI, along with identifying common challenges in payment applications. It is intended solely for academic and research purposes and should not be used for making business decisions.

#### [PhonePe](https://www.phonepe.com/)

PhonePe is an all-encompassing payment application that empowers you to conduct financial transactions effortlessly using BHIM UPI, credit or debit cards, and its in-built wallet. It streamlines various payments such as mobile recharges, utility bill settlements, and shopping at your preferred online and offline merchants. Beyond payments, PhonePe extends its services to financial investments like mutual funds and insurance plans, including vehicle insurance directly through the app. By linking your bank account to PhonePe, you can enjoy instant money transfers via BHIM UPI. The app prioritizes user safety and security, offering a robust alternative to traditional internet banking while catering to a broad spectrum of your payment, investment, and banking requirements.

#### [Google Pay (Gpay)](https://pay.google.com/about/)

Google Pay serves as an integrated and secure digital payment platform, aimed at refining and simplifying your financial transactions and management. It facilitates seamless contactless payments across a wide range of venues, immediate money transfers among peers, and access to exclusive deals and rewards from your favored establishments. Google Pay goes further by providing analytical tools to track and manage your spending, offering comprehensive transaction summaries and valuable financial insights linked to your accounts. With a focus on user-friendliness, transactional privacy, and smooth integration with e-commerce, Google Pay stands out as a versatile solution for handling daily payments and overseeing personal finance efficiently.

# Understanding the Mechanics of Payment Apps
![alt text](https://substackcdn.com/image/fetch/f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fbucketeer-e05bbc84-baa3-437e-9518-adb32be77984.s3.amazonaws.com%2Fpublic%2Fimages%2F60eedf58-289e-4409-a414-c65fb10beece_1006x1280.png)
# Industry Analysis & Business Insight
PhonePe and Google’s local payments services — controlled, on average, 80-85% of UPI volumes every month. NPCI data as of December 2023 shows PhonePe had a 46% share in UPI volumes, followed by Google Pay at 36% and Paytm Payments Bank at 13%.

![alt text](https://img.etimg.com/photo/msid-107407765/upi-market-share-by-volume.jpg)
<p float="left">
<img src="/images/UPI_txn_value.png" width="425"/>
<img src="/images/UPI_txn_volume.png" width="425"/> 
<\p>



# Overview of Customer Experience Analyzer Framework
## Data Extraction Pipeline

Currently, my analysis is based solely on **reviews from the Google Play Store and Apple App Store**. This approach could be expanded to incorporate feedback from public forums, social media monitoring, and internal company data.

> [!NOTE]
> During the extraction process, there may be instances where some reviews are not captured due to occasional malfunctions of the crawler. As a result, the number of reviews collected might not accurately reflect the total number of reviews available.

[PhonePe Reviews](https://play.google.com/store/apps/details?id=com.phonepe.app&hl=en_IN&gl=US)   
[Google Pay Reviews](https://play.google.com/store/apps/details?id=com.google.android.apps.nbu.paisa.user&hl=en&gl=US)

## Creating Generative Pre-Trained Transformer Framework
### Providing Context of Business

### Prompt Engineering 
In the domain of artificial intelligence, particularly within the spheres of Natural Language Processing (NLP) and the latest generative AI technologies such as GPT-3 and DALL-E, prompt engineering emerges as an indispensable discipline. This specialized field entails the strategic formulation of inputs, or "prompts," tailored to direct AI towards generating specific, desired outputs. The practice of prompt engineering is characterized by a methodical, iterative approach, necessitating a series of well-defined steps to refine prompts and achieve precise results. This process is crucial for professionals seeking to harness the full potential of AI in producing accurate and contextually relevant responses.

![alt text](https://pathmonk.com/wp-content/uploads/2023/08/Prompt-Engineering-Effectively-A-Marketers-Guide-to-Mastering-Prompt-Engineering-1024x585.png)
> [!TIP]
> Prompt engineering is particularly effective in scenarios with limited or non-existent labeled data, offering a streamlined approach to crafting solutions with minimal time and effort. By guiding AI models through precise inputs, it enhances response relevance and efficiency, making it a valuable tool in developing agile and targeted AI applications. 
## Analysing Reviews 
    1. Generating Tags, 
    2. Tagging Emotional Tone 
    3. Critical Issues
    4. Feature failures 
    5. Customer Suggestion
    6. Escalations

## Generating Actionable Insights

## Creating a Streamlit app for tracking issues 



# Competitior Analysis - Comparing Phone vs Google Pay


> [!NOTE]
> Useful information that users should know, even when skimming content.

> [!TIP]
> Helpful advice for doing things better or more easily.

> [!IMPORTANT]
> Key information users need to know to achieve their goal.

> [!WARNING]
> Urgent info that needs immediate user attention to avoid problems.

> [!CAUTION]
> Advises about risks or negative outcomes of certain actions.


Image References:

https://www.gosurvey.in/media/a0vmcbf1/customer-experience-is-important-for-businesses.jpg
https://economictimes.indiatimes.com/tech/technology/paytm-crisis-upi-market-share-cap-rule-in-focus-leaders-may-corner-a-bigger-pie/articleshow/107406233.cms?utm_source=contentofinterest&utm_medium=text&utm_campaign=cppst

