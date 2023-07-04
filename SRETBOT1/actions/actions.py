# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk.events import SlotSet
from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.types import DomainDict
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class Action_specific_fees(Action):
    def name(self) -> Text:
        return "Action_explain_specific_fees"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        course={"aida":"2,50,000Rs for Btech and 75,000 for Bsc","aiml":"2,50,000Rs for Btech","cybsec":"2,50,000Rs","medsci":"2,50,000Rs","bioinfomatics":"75,000Rs", "da":"75,000Rs"}

        inter_c=tracker.get_slot("interested_course")
        if inter_c is not None: 
            inter_c=inter_c.lower()
        if inter_c in course:
            res = course[inter_c]
            dispatcher.utter_message(text=res)
        else:
            dispatcher.utter_message(text="Course fees information not found. Please try again")
        return[]

class Action_Give_Depth_Info(Action):
    def name(self) -> Text:
        return "Action_Give_Depth_Info"
    def run(self, dispatcher: CollectingDispatcher,tracker: Tracker,domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        values ={"aiml":"Artifical Intelligence and Machine Learning:\nArtificial Intelligence (AI) and Machine Learning (ML) are transformative technologies that have revolutionized various industries and are shaping the future of technology. Artificial intelligence refers to the development of intelligent systems that can perform tasks that normally require human intelligence, such as speech recognition, image processing, and decision making. ML, a subset of artificial intelligence, focuses on algorithms and statistical models that allow computers to learn and make predictions or decisions without special programming.\n\n Artificial intelligence and ML have made significant advances in areas such as natural language processing, computer vision, robotics and data analytics. They have opened up new opportunities in healthcare, finance, transportation, manufacturing and many other areas. AI-powered applications increase efficiency, automate processes, improve decision-making and enable personalized experiences.",
                 "aida":"Artifical Intelligence and Data Analytics:\nArtificial Intelligence (AI) and Data Analytics are two interconnected fields that are shaping the way businesses operate and make decisions in the digital age. AI refers to the development of intelligent systems that can perform tasks requiring human-like intelligence, such as learning, reasoning, and problem-solving. Data Analytics, on the other hand, focuses on extracting meaningful insights from large volumes of data to drive informed decision-making. \n\n AI and Data Analytics work hand in hand to unlock the full potential of data. AI techniques, including machine learning and deep learning, enable the analysis of vast amounts of data to uncover patterns, trends, and correlations that may not be apparent to human analysts. This helps businesses gain valuable insights, make accurate predictions, and optimize processes.",
                 "cybsec":"Cybersecurity & Internet of Things:\nCybersecurity and the Internet of Things (IoT) are two interconnected domains that play a crucial role in the digital era, where the proliferation of connected devices poses significant security challenges. Cybersecurity focuses on protecting computer systems, networks, and data from unauthorized access, breaches, and malicious activities. IoT refers to the network of interconnected devices embedded with sensors, software, and connectivity that enable them to collect and exchange data.\n\nAs the IoT ecosystem expands, with billions of devices being connected, ensuring the security and privacy of these devices and the data they generate becomes paramount. Cybersecurity in the context of IoT involves implementing robust security measures throughout the entire lifecycle of IoT devices, from design and development to deployment and operation. This includes authentication and access control mechanisms, encryption protocols, secure communication channels, and monitoring systems to detect and respond to security incidents",
                 "medsci":"Medical science:\nYet to be updated\n\n\n\n",
                 'bioinfomatics':"Bioinformatics:\nIt is a multidisciplinary field that combines biology, computer science, and information technology to analyze and interpret biological data. It involves the development and application of computational methods, algorithms, and tools to study biological systems, including genes, proteins, and genomes. Bioinformatics plays a crucial role in understanding biological processes, unraveling complex relationships within biological data, and facilitating advancements in various areas of life sciences.\n\nIn bioinformatics, vast amounts of biological data are collected and processed, including DNA sequences, protein structures, gene expression profiles, and clinical data. By applying computational techniques, researchers can extract meaningful insights from this data, leading to discoveries in genomics, proteomics, evolutionary biology, and drug discovery. Bioinformatics tools and algorithms enable the analysis of large datasets, identification of patterns and trends, prediction of protein structures and functions, and exploration of genetic variations and disease associations.",
                 "da":"Data analytics\nIt is the process of examining and interpreting large volumes of data to uncover valuable insights, patterns, and trends that can inform decision-making and drive business outcomes. It involves applying various statistical and computational techniques to transform raw data into meaningful information and actionable intelligence.\n\nIn today's data-driven world, organizations collect and store vast amounts of data from various sources, including customer interactions, sales transactions, social media, sensors, and more. Data analytics helps extract valuable insights from this data, enabling businesses to understand customer behavior, optimize operations, identify market trends, and make data-driven strategic decisions.\n\nData analytics encompasses different approaches, including descriptive analytics, which focuses on summarizing and visualizing data to gain an overview of past events and trends. It also includes diagnostic analytics, which involves analyzing data to understand why certain events or outcomes occurred. Predictive analytics utilizes historical data and statistical models to forecast future trends and outcomes, while prescriptive analytics goes a step further by recommending actions and strategies based on the insights generated."
                 }
        inter_c=tracker.get_slot("interested_course")
        if inter_c is None:
            res="AIML:\n Artificial Intelligence (AI) and Machine Learning (ML) are transformative technologies that have revolutionized various industries and are shaping the future of technology. Artificial intelligence refers to the development of intelligent systems that can perform tasks that normally require human intelligence, such as speech recognition, image processing, and decision making. ML, a subset of artificial intelligence, focuses on algorithms and statistical models that allow computers to learn and make predictions or decisions without special programming.\n\n Artificial intelligence and ML have made significant advances in areas such as natural language processing, computer vision, robotics and data analytics. They have opened up new opportunities in healthcare, finance, transportation, manufacturing and many other areas. AI-powered applications increase efficiency, automate processes, improve decision-making and enable personalized experiences.\n\n\n\n AIDA:\n Artificial Intelligence (AI) and Data Analytics are two interconnected fields that are shaping the way businesses operate and make decisions in the digital age. AI refers to the development of intelligent systems that can perform tasks requiring human-like intelligence, such as learning, reasoning, and problem-solving. Data Analytics, on the other hand, focuses on extracting meaningful insights from large volumes of data to drive informed decision-making. \n\n AI and Data Analytics work hand in hand to unlock the full potential of data. AI techniques, including machine learning and deep learning, enable the analysis of vast amounts of data to uncover patterns, trends, and correlations that may not be apparent to human analysts. This helps businesses gain valuable insights, make accurate predictions, and optimize processes. \n\n\n\n CYB&IOT: \nCybersecurity and the Internet of Things (IoT) are two interconnected domains that play a crucial role in the digital era, where the proliferation of connected devices poses significant security challenges. Cybersecurity focuses on protecting computer systems, networks, and data from unauthorized access, breaches, and malicious activities. IoT refers to the network of interconnected devices embedded with sensors, software, and connectivity that enable them to collect and exchange data.\n\nAs the IoT ecosystem expands, with billions of devices being connected, ensuring the security and privacy of these devices and the data they generate becomes paramount. Cybersecurity in the context of IoT involves implementing robust security measures throughout the entire lifecycle of IoT devices, from design and development to deployment and operation. This includes authentication and access control mechanisms, encryption protocols, secure communication channels, and monitoring systems to detect and respond to security incidents\n\n\n\n Medical science:\nYet to be updated\n\n\n\n BioInfomatics: \nBioinformatics is a multidisciplinary field that combines biology, computer science, and information technology to analyze and interpret biological data. It involves the development and application of computational methods, algorithms, and tools to study biological systems, including genes, proteins, and genomes. Bioinformatics plays a crucial role in understanding biological processes, unraveling complex relationships within biological data, and facilitating advancements in various areas of life sciences.\n\nIn bioinformatics, vast amounts of biological data are collected and processed, including DNA sequences, protein structures, gene expression profiles, and clinical data. By applying computational techniques, researchers can extract meaningful insights from this data, leading to discoveries in genomics, proteomics, evolutionary biology, and drug discovery. Bioinformatics tools and algorithms enable the analysis of large datasets, identification of patterns and trends, prediction of protein structures and functions, and exploration of genetic variations and disease associations.\n\n\n\n Data Analytics:\nData analytics is the process of examining and interpreting large volumes of data to uncover valuable insights, patterns, and trends that can inform decision-making and drive business outcomes. It involves applying various statistical and computational techniques to transform raw data into meaningful information and actionable intelligence.\n\nIn today's data-driven world, organizations collect and store vast amounts of data from various sources, including customer interactions, sales transactions, social media, sensors, and more. Data analytics helps extract valuable insights from this data, enabling businesses to understand customer behavior, optimize operations, identify market trends, and make data-driven strategic decisions.\n\nData analytics encompasses different approaches, including descriptive analytics, which focuses on summarizing and visualizing data to gain an overview of past events and trends. It also includes diagnostic analytics, which involves analyzing data to understand why certain events or outcomes occurred. Predictive analytics utilizes historical data and statistical models to forecast future trends and outcomes, while prescriptive analytics goes a step further by recommending actions and strategies based on the insights generated."
            dispatcher.utter_message(text=res)
            return[]
        if inter_c is not None: 
            inter_c=inter_c.lower()
        if inter_c in values:
            res = values[inter_c]
            dispatcher.utter_message(text=res)
        else:
            dispatcher.utter_message(text="Course fees information not found. Please try again")
        return[]