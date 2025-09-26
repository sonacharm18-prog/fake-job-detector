{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "40c20abc-d31a-4a86-b8d0-b3c65f0251a2",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting wordcloud\n",
      "  Downloading wordcloud-1.9.4-cp312-cp312-win_amd64.whl.metadata (3.5 kB)\n",
      "Requirement already satisfied: numpy>=1.6.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from wordcloud) (1.26.4)\n",
      "Requirement already satisfied: pillow in c:\\users\\hp\\anaconda3\\lib\\site-packages (from wordcloud) (10.4.0)\n",
      "Requirement already satisfied: matplotlib in c:\\users\\hp\\anaconda3\\lib\\site-packages (from wordcloud) (3.9.2)\n",
      "Requirement already satisfied: contourpy>=1.0.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from matplotlib->wordcloud) (1.2.0)\n",
      "Requirement already satisfied: cycler>=0.10 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from matplotlib->wordcloud) (0.11.0)\n",
      "Requirement already satisfied: fonttools>=4.22.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from matplotlib->wordcloud) (4.51.0)\n",
      "Requirement already satisfied: kiwisolver>=1.3.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from matplotlib->wordcloud) (1.4.4)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from matplotlib->wordcloud) (24.1)\n",
      "Requirement already satisfied: pyparsing>=2.3.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from matplotlib->wordcloud) (3.1.2)\n",
      "Requirement already satisfied: python-dateutil>=2.7 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from matplotlib->wordcloud) (2.9.0.post0)\n",
      "Requirement already satisfied: six>=1.5 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from python-dateutil>=2.7->matplotlib->wordcloud) (1.16.0)\n",
      "Downloading wordcloud-1.9.4-cp312-cp312-win_amd64.whl (301 kB)\n",
      "Installing collected packages: wordcloud\n",
      "Successfully installed wordcloud-1.9.4\n"
     ]
    }
   ],
   "source": [
    "!pip install wordcloud"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "a7ca4d76-b014-4102-b4c8-9d90d97d867e",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Requirement already satisfied: spacy in c:\\users\\hp\\anaconda3\\lib\\site-packages (3.8.7)\n",
      "Requirement already satisfied: spacy-legacy<3.1.0,>=3.0.11 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (3.0.12)\n",
      "Requirement already satisfied: spacy-loggers<2.0.0,>=1.0.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (1.0.5)\n",
      "Requirement already satisfied: murmurhash<1.1.0,>=0.28.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (1.0.13)\n",
      "Requirement already satisfied: cymem<2.1.0,>=2.0.2 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (2.0.11)\n",
      "Requirement already satisfied: preshed<3.1.0,>=3.0.2 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (3.0.10)\n",
      "Requirement already satisfied: thinc<8.4.0,>=8.3.4 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (8.3.6)\n",
      "Requirement already satisfied: wasabi<1.2.0,>=0.9.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (1.1.3)\n",
      "Requirement already satisfied: srsly<3.0.0,>=2.4.3 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (2.5.1)\n",
      "Requirement already satisfied: catalogue<2.1.0,>=2.0.6 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (2.0.10)\n",
      "Requirement already satisfied: weasel<0.5.0,>=0.1.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (0.4.1)\n",
      "Requirement already satisfied: typer<1.0.0,>=0.3.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (0.9.0)\n",
      "Requirement already satisfied: tqdm<5.0.0,>=4.38.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (4.66.5)\n",
      "Requirement already satisfied: numpy>=1.19.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (2.3.3)\n",
      "Requirement already satisfied: requests<3.0.0,>=2.13.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (2.32.3)\n",
      "Requirement already satisfied: pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (2.8.2)\n",
      "Requirement already satisfied: jinja2 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (3.1.4)\n",
      "Requirement already satisfied: setuptools in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (75.1.0)\n",
      "Requirement already satisfied: packaging>=20.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (24.1)\n",
      "Requirement already satisfied: langcodes<4.0.0,>=3.2.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from spacy) (3.5.0)\n",
      "Requirement already satisfied: language-data>=1.2 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from langcodes<4.0.0,>=3.2.0->spacy) (1.3.0)\n",
      "Requirement already satisfied: annotated-types>=0.4.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy) (0.6.0)\n",
      "Requirement already satisfied: pydantic-core==2.20.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy) (2.20.1)\n",
      "Requirement already satisfied: typing-extensions>=4.6.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from pydantic!=1.8,!=1.8.1,<3.0.0,>=1.7.4->spacy) (4.11.0)\n",
      "Requirement already satisfied: charset-normalizer<4,>=2 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from requests<3.0.0,>=2.13.0->spacy) (3.3.2)\n",
      "Requirement already satisfied: idna<4,>=2.5 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from requests<3.0.0,>=2.13.0->spacy) (3.7)\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from requests<3.0.0,>=2.13.0->spacy) (2.2.3)\n",
      "Requirement already satisfied: certifi>=2017.4.17 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from requests<3.0.0,>=2.13.0->spacy) (2025.8.3)\n",
      "Requirement already satisfied: blis<1.4.0,>=1.3.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from thinc<8.4.0,>=8.3.4->spacy) (1.3.0)\n",
      "Requirement already satisfied: confection<1.0.0,>=0.0.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from thinc<8.4.0,>=8.3.4->spacy) (0.1.5)\n",
      "Requirement already satisfied: colorama in c:\\users\\hp\\anaconda3\\lib\\site-packages (from tqdm<5.0.0,>=4.38.0->spacy) (0.4.6)\n",
      "Requirement already satisfied: click<9.0.0,>=7.1.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from typer<1.0.0,>=0.3.0->spacy) (8.1.7)\n",
      "Requirement already satisfied: cloudpathlib<1.0.0,>=0.7.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from weasel<0.5.0,>=0.1.0->spacy) (0.22.0)\n",
      "Requirement already satisfied: smart-open<8.0.0,>=5.2.1 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from weasel<0.5.0,>=0.1.0->spacy) (5.2.1)\n",
      "Requirement already satisfied: MarkupSafe>=2.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from jinja2->spacy) (2.1.3)\n",
      "Requirement already satisfied: marisa-trie>=1.1.0 in c:\\users\\hp\\anaconda3\\lib\\site-packages (from language-data>=1.2->langcodes<4.0.0,>=3.2.0->spacy) (1.3.1)\n"
     ]
    }
   ],
   "source": [
    "!pip install -U spacy"
   ]
  },
  {
   "cell_type": "code",
   "id": "39cca951-7752-4c12-8f50-2cec2bee7dc3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import re\n",
    "import string\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import random\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n",
    "from sklearn.feature_extraction.text import TfidVectorizer, CountVectorizer\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.base import TransformerMixin\n",
    "from sklearn.metrics import accuracy_score,plot_confusion_matrix,classification_report,confusion_matrix\n",
    "from wordcloud import WordCloud\n",
    "import spacy\n",
    "from spacy.lang.en.stop_words import STOP_WORDS\n",
    "from spacy.lang.en import English"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "id": "21836f1a-627e-4455-8d4a-b681a79ad523",
   "metadata": {},
   "outputs": [],
   "source": [
    "df=pd.read_csv(r'C:\\Users\\HP\\Downloads\\fakejob.csv')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "id": "b4ee6260-0c86-4425-bb7a-20d418b6ba3e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>job_id</th>\n",
       "      <th>title</th>\n",
       "      <th>location</th>\n",
       "      <th>department</th>\n",
       "      <th>salary_range</th>\n",
       "      <th>company_profile</th>\n",
       "      <th>description</th>\n",
       "      <th>requirements</th>\n",
       "      <th>benefits</th>\n",
       "      <th>telecommuting</th>\n",
       "      <th>has_company_logo</th>\n",
       "      <th>has_questions</th>\n",
       "      <th>employment_type</th>\n",
       "      <th>required_experience</th>\n",
       "      <th>required_education</th>\n",
       "      <th>industry</th>\n",
       "      <th>function</th>\n",
       "      <th>fraudulent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Marketing Intern</td>\n",
       "      <td>US, NY, New York</td>\n",
       "      <td>Marketing</td>\n",
       "      <td>NaN</td>\n",
       "      <td>We're Food52, and we've created a groundbreaki...</td>\n",
       "      <td>Food52, a fast-growing, James Beard Award-winn...</td>\n",
       "      <td>Experience with content management systems a m...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Other</td>\n",
       "      <td>Internship</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Marketing</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Customer Service - Cloud Video Production</td>\n",
       "      <td>NZ, , Auckland</td>\n",
       "      <td>Success</td>\n",
       "      <td>NaN</td>\n",
       "      <td>90 Seconds, the worlds Cloud Video Production ...</td>\n",
       "      <td>Organised - Focused - Vibrant - Awesome!Do you...</td>\n",
       "      <td>What we expect from you:Your key responsibilit...</td>\n",
       "      <td>What you will get from usThrough being part of...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Full-time</td>\n",
       "      <td>Not Applicable</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Marketing and Advertising</td>\n",
       "      <td>Customer Service</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Commissioning Machinery Assistant (CMA)</td>\n",
       "      <td>US, IA, Wever</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Valor Services provides Workforce Solutions th...</td>\n",
       "      <td>Our client, located in Houston, is actively se...</td>\n",
       "      <td>Implement pre-commissioning and commissioning ...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Account Executive - Washington DC</td>\n",
       "      <td>US, DC, Washington</td>\n",
       "      <td>Sales</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Our passion for improving quality of life thro...</td>\n",
       "      <td>THE COMPANY: ESRI – Environmental Systems Rese...</td>\n",
       "      <td>EDUCATION: Bachelor’s or Master’s in GIS, busi...</td>\n",
       "      <td>Our culture is anything but corporate—we have ...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Full-time</td>\n",
       "      <td>Mid-Senior level</td>\n",
       "      <td>Bachelor's Degree</td>\n",
       "      <td>Computer Software</td>\n",
       "      <td>Sales</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Bill Review Manager</td>\n",
       "      <td>US, FL, Fort Worth</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>SpotSource Solutions LLC is a Global Human Cap...</td>\n",
       "      <td>JOB TITLE: Itemization Review ManagerLOCATION:...</td>\n",
       "      <td>QUALIFICATIONS:RN license in the State of Texa...</td>\n",
       "      <td>Full Benefits Offered</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Full-time</td>\n",
       "      <td>Mid-Senior level</td>\n",
       "      <td>Bachelor's Degree</td>\n",
       "      <td>Hospital &amp; Health Care</td>\n",
       "      <td>Health Care Provider</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   job_id                                      title            location  \\\n",
       "0       1                           Marketing Intern    US, NY, New York   \n",
       "1       2  Customer Service - Cloud Video Production      NZ, , Auckland   \n",
       "2       3    Commissioning Machinery Assistant (CMA)       US, IA, Wever   \n",
       "3       4          Account Executive - Washington DC  US, DC, Washington   \n",
       "4       5                        Bill Review Manager  US, FL, Fort Worth   \n",
       "\n",
       "  department salary_range                                    company_profile  \\\n",
       "0  Marketing          NaN  We're Food52, and we've created a groundbreaki...   \n",
       "1    Success          NaN  90 Seconds, the worlds Cloud Video Production ...   \n",
       "2        NaN          NaN  Valor Services provides Workforce Solutions th...   \n",
       "3      Sales          NaN  Our passion for improving quality of life thro...   \n",
       "4        NaN          NaN  SpotSource Solutions LLC is a Global Human Cap...   \n",
       "\n",
       "                                         description  \\\n",
       "0  Food52, a fast-growing, James Beard Award-winn...   \n",
       "1  Organised - Focused - Vibrant - Awesome!Do you...   \n",
       "2  Our client, located in Houston, is actively se...   \n",
       "3  THE COMPANY: ESRI – Environmental Systems Rese...   \n",
       "4  JOB TITLE: Itemization Review ManagerLOCATION:...   \n",
       "\n",
       "                                        requirements  \\\n",
       "0  Experience with content management systems a m...   \n",
       "1  What we expect from you:Your key responsibilit...   \n",
       "2  Implement pre-commissioning and commissioning ...   \n",
       "3  EDUCATION: Bachelor’s or Master’s in GIS, busi...   \n",
       "4  QUALIFICATIONS:RN license in the State of Texa...   \n",
       "\n",
       "                                            benefits  telecommuting  \\\n",
       "0                                                NaN              0   \n",
       "1  What you will get from usThrough being part of...              0   \n",
       "2                                                NaN              0   \n",
       "3  Our culture is anything but corporate—we have ...              0   \n",
       "4                              Full Benefits Offered              0   \n",
       "\n",
       "   has_company_logo  has_questions employment_type required_experience  \\\n",
       "0                 1              0           Other          Internship   \n",
       "1                 1              0       Full-time      Not Applicable   \n",
       "2                 1              0             NaN                 NaN   \n",
       "3                 1              0       Full-time    Mid-Senior level   \n",
       "4                 1              1       Full-time    Mid-Senior level   \n",
       "\n",
       "  required_education                   industry              function  \\\n",
       "0                NaN                        NaN             Marketing   \n",
       "1                NaN  Marketing and Advertising      Customer Service   \n",
       "2                NaN                        NaN                   NaN   \n",
       "3  Bachelor's Degree          Computer Software                 Sales   \n",
       "4  Bachelor's Degree     Hospital & Health Care  Health Care Provider   \n",
       "\n",
       "   fraudulent  \n",
       "0           0  \n",
       "1           0  \n",
       "2           0  \n",
       "3           0  \n",
       "4           0  "
      ]
     },
     "execution_count": 29,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 31,
   "id": "79085a3c-0262-47da-a90a-378fa7375b49",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(17880, 18)"
      ]
     },
     "execution_count": 31,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 33,
   "id": "b6e57ea7-8f1a-48d6-b2f7-4218ba0f6a44",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "job_id                     0\n",
       "title                      0\n",
       "location                 346\n",
       "department             11547\n",
       "salary_range           15012\n",
       "company_profile         3308\n",
       "description                1\n",
       "requirements            2696\n",
       "benefits                7212\n",
       "telecommuting              0\n",
       "has_company_logo           0\n",
       "has_questions              0\n",
       "employment_type         3471\n",
       "required_experience     7050\n",
       "required_education      8105\n",
       "industry                4903\n",
       "function                6455\n",
       "fraudulent                 0\n",
       "dtype: int64"
      ]
     },
     "execution_count": 33,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.isnull().sum()"
   ]
  },
  {
   "cell_type": "code",
   "id": "c13a99d1-8bea-4d47-aa1f-0e072dad2631",
   "metadata": {},
   "outputs": [],
   "source": [
    "columns=['job_id','telecommuting','has_company-logo','has_questions','salary_range','employment_type']\n",
    "for colu in columns:\n",
    "    del df[colu]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "id": "f4c1c758-ee9e-4f9b-99f4-a29290a9df28",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>job_id</th>\n",
       "      <th>title</th>\n",
       "      <th>location</th>\n",
       "      <th>department</th>\n",
       "      <th>salary_range</th>\n",
       "      <th>company_profile</th>\n",
       "      <th>description</th>\n",
       "      <th>requirements</th>\n",
       "      <th>benefits</th>\n",
       "      <th>telecommuting</th>\n",
       "      <th>has_company_logo</th>\n",
       "      <th>has_questions</th>\n",
       "      <th>employment_type</th>\n",
       "      <th>required_experience</th>\n",
       "      <th>required_education</th>\n",
       "      <th>industry</th>\n",
       "      <th>function</th>\n",
       "      <th>fraudulent</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>1</td>\n",
       "      <td>Marketing Intern</td>\n",
       "      <td>US, NY, New York</td>\n",
       "      <td>Marketing</td>\n",
       "      <td>NaN</td>\n",
       "      <td>We're Food52, and we've created a groundbreaki...</td>\n",
       "      <td>Food52, a fast-growing, James Beard Award-winn...</td>\n",
       "      <td>Experience with content management systems a m...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Other</td>\n",
       "      <td>Internship</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Marketing</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>2</td>\n",
       "      <td>Customer Service - Cloud Video Production</td>\n",
       "      <td>NZ, , Auckland</td>\n",
       "      <td>Success</td>\n",
       "      <td>NaN</td>\n",
       "      <td>90 Seconds, the worlds Cloud Video Production ...</td>\n",
       "      <td>Organised - Focused - Vibrant - Awesome!Do you...</td>\n",
       "      <td>What we expect from you:Your key responsibilit...</td>\n",
       "      <td>What you will get from usThrough being part of...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Full-time</td>\n",
       "      <td>Not Applicable</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Marketing and Advertising</td>\n",
       "      <td>Customer Service</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>3</td>\n",
       "      <td>Commissioning Machinery Assistant (CMA)</td>\n",
       "      <td>US, IA, Wever</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Valor Services provides Workforce Solutions th...</td>\n",
       "      <td>Our client, located in Houston, is actively se...</td>\n",
       "      <td>Implement pre-commissioning and commissioning ...</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>4</td>\n",
       "      <td>Account Executive - Washington DC</td>\n",
       "      <td>US, DC, Washington</td>\n",
       "      <td>Sales</td>\n",
       "      <td>NaN</td>\n",
       "      <td>Our passion for improving quality of life thro...</td>\n",
       "      <td>THE COMPANY: ESRI – Environmental Systems Rese...</td>\n",
       "      <td>EDUCATION: Bachelor’s or Master’s in GIS, busi...</td>\n",
       "      <td>Our culture is anything but corporate—we have ...</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>0</td>\n",
       "      <td>Full-time</td>\n",
       "      <td>Mid-Senior level</td>\n",
       "      <td>Bachelor's Degree</td>\n",
       "      <td>Computer Software</td>\n",
       "      <td>Sales</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>5</td>\n",
       "      <td>Bill Review Manager</td>\n",
       "      <td>US, FL, Fort Worth</td>\n",
       "      <td>NaN</td>\n",
       "      <td>NaN</td>\n",
       "      <td>SpotSource Solutions LLC is a Global Human Cap...</td>\n",
       "      <td>JOB TITLE: Itemization Review ManagerLOCATION:...</td>\n",
       "      <td>QUALIFICATIONS:RN license in the State of Texa...</td>\n",
       "      <td>Full Benefits Offered</td>\n",
       "      <td>0</td>\n",
       "      <td>1</td>\n",
       "      <td>1</td>\n",
       "      <td>Full-time</td>\n",
       "      <td>Mid-Senior level</td>\n",
       "      <td>Bachelor's Degree</td>\n",
       "      <td>Hospital &amp; Health Care</td>\n",
       "      <td>Health Care Provider</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   job_id                                      title            location  \\\n",
       "0       1                           Marketing Intern    US, NY, New York   \n",
       "1       2  Customer Service - Cloud Video Production      NZ, , Auckland   \n",
       "2       3    Commissioning Machinery Assistant (CMA)       US, IA, Wever   \n",
       "3       4          Account Executive - Washington DC  US, DC, Washington   \n",
       "4       5                        Bill Review Manager  US, FL, Fort Worth   \n",
       "\n",
       "  department salary_range                                    company_profile  \\\n",
       "0  Marketing          NaN  We're Food52, and we've created a groundbreaki...   \n",
       "1    Success          NaN  90 Seconds, the worlds Cloud Video Production ...   \n",
       "2        NaN          NaN  Valor Services provides Workforce Solutions th...   \n",
       "3      Sales          NaN  Our passion for improving quality of life thro...   \n",
       "4        NaN          NaN  SpotSource Solutions LLC is a Global Human Cap...   \n",
       "\n",
       "                                         description  \\\n",
       "0  Food52, a fast-growing, James Beard Award-winn...   \n",
       "1  Organised - Focused - Vibrant - Awesome!Do you...   \n",
       "2  Our client, located in Houston, is actively se...   \n",
       "3  THE COMPANY: ESRI – Environmental Systems Rese...   \n",
       "4  JOB TITLE: Itemization Review ManagerLOCATION:...   \n",
       "\n",
       "                                        requirements  \\\n",
       "0  Experience with content management systems a m...   \n",
       "1  What we expect from you:Your key responsibilit...   \n",
       "2  Implement pre-commissioning and commissioning ...   \n",
       "3  EDUCATION: Bachelor’s or Master’s in GIS, busi...   \n",
       "4  QUALIFICATIONS:RN license in the State of Texa...   \n",
       "\n",
       "                                            benefits  telecommuting  \\\n",
       "0                                                NaN              0   \n",
       "1  What you will get from usThrough being part of...              0   \n",
       "2                                                NaN              0   \n",
       "3  Our culture is anything but corporate—we have ...              0   \n",
       "4                              Full Benefits Offered              0   \n",
       "\n",
       "   has_company_logo  has_questions employment_type required_experience  \\\n",
       "0                 1              0           Other          Internship   \n",
       "1                 1              0       Full-time      Not Applicable   \n",
       "2                 1              0             NaN                 NaN   \n",
       "3                 1              0       Full-time    Mid-Senior level   \n",
       "4                 1              1       Full-time    Mid-Senior level   \n",
       "\n",
       "  required_education                   industry              function  \\\n",
       "0                NaN                        NaN             Marketing   \n",
       "1                NaN  Marketing and Advertising      Customer Service   \n",
       "2                NaN                        NaN                   NaN   \n",
       "3  Bachelor's Degree          Computer Software                 Sales   \n",
       "4  Bachelor's Degree     Hospital & Health Care  Health Care Provider   \n",
       "\n",
       "   fraudulent  \n",
       "0           0  \n",
       "1           0  \n",
       "2           0  \n",
       "3           0  \n",
       "4           0  "
      ]
     },
     "execution_count": 35,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "c56237f8-f5c8-40d8-92d2-cde95a828053",
   "metadata": {},
   "outputs": [],
   "source": [
    " df.fillna('',inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "c977845e-cf71-42de-9ac3-730d45451b99",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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YgAAAACsVdIzxO64445NfuKjjjpqk48FAAAAgM1tk4LY0UcfvUkPVigU1vsNlAAAAACwpdikINba2trRcwAAAADAZlFR7gEAAAAAYHNq97dMXnDBBRvd/8Mf/vAzDwMAAAAAHa3dQey2225rc7ulpSUaGxujsrIydtllF0EMAAAAgC1au4PYwoUL19nW3NwcJ554YhxzzDElGQoAAAAAOkpJriFWW1sbF1xwQZx33nmleDgAAAAA6DAlu6j+u+++G01NTaV6OAAAAADoEO3+yOQVV1zR5nZKKZYuXRr//d//HWPHji3ZYAAAAADQEdodxC699NI2tysqKmK77baLCRMmxDnnnFOywQAAAACgI7Q7iDU2NnbEHAAAAACwWZTsGmIAAAAA0Bls0hlixx577CY/4IwZMz7zMAAAAADQ0TbpDLG6urriT21tbcyePTsef/zx4v758+fH7Nmzo66ursMGBQAAAIBS2KQzxG644YbiP0+bNi2+9a1vxfTp06Nbt24REbFmzZqYOHFi1NbWdsyUAAAAAFAihZRSas8dtttuu3j44Yfjr/7qr9psf/bZZ+OAAw6It956q6QDbkxzc3PU1dVFU1OTGAcAAACQuU1tRe2+qP7q1avj6aefXmf7008/Ha2tre19OAAAAADYrDbpI5N/6aSTToqTTz45Xnjhhdhvv/0iIuLRRx+Niy66KE466aSSDwgAAAAApdTuIPbv//7vMWDAgLj00ktj6dKlERGx/fbbx1lnnRVnnnlmyQcEAAAAgFJq9zXE/lJzc3NERNmu3+UaYgAAAACstamtqN1niP0lEQoAAACAzqbdQWzIkCFRKBQ2uP+ll176XAMBAAAAQEdqdxCbMmVKm9stLS2xcOHCuOeee2Lq1KmlmgsAAAAAOkS7g9jkyZPXu/2nP/1pPP744597IAAAAADoSBWleqDDDjssbr311lI9HAAAAAB0iJIFsf/5n/+J3r17l+rhAAAAAKBDtPsjk8OHD29zUf2UUixbtiz+9Kc/xVVXXVXS4QAAAACg1NodxI4++ug2tysqKmK77baL0aNHx9ChQ0s1FwAAAAB0iEJKKZV7iM+qubk56urqYtip06Nbdc9yj9Nh5v+fE8o9AgAAAMAWb20rampqitra2g0e1+4zxP7Shx9+GC0tLW22bezJAAAAAKDc2n1R/ffffz8mTZoU/fr1i6233jq23XbbNj8AAAAAsCVrdxA766yz4v7774+rrroqqqur47rrrot//dd/jfr6+rjppps6YkYAAAAAKJl2f2TyN7/5Tdx0000xevToOPnkk+MrX/lK7LrrrjF48OD4+c9/HuPGjeuIOQEAAACgJNp9htjbb78dQ4YMiYiPrxf29ttvR0TEgQceGHPnzi3tdAAAAABQYu0OYjvvvHO8/PLLERGxxx57xK9+9auI+PjMsW222aaUswEAAABAybU7iJ100knxhz/8ISIizjnnnOK1xE4//fSYOnVqyQcEAAAAgFJq9zXETj/99OI/jxkzJp555pl4/PHHY5dddolhw4aVdDgAAAAAKLV2nSHW0tISY8aMieeee664bdCgQXHssceKYQAAAAB0Cu0KYt27d4/FixdHoVDoqHkAAAAAoEO1+xpiJ5xwQlx//fUdMQsAAAAAdLh2X0Ns1apVcd1118XMmTNj5MiR0atXrzb7L7nkkpINBwAAAACltklB7IknnoiGhoaoqKiIxYsXx5e+9KWIiDbXEosIH6UEAAAAYIu3SUFs+PDhsXTp0ujXr1+88sor8fvf/z769OnT0bMBAAAAQMlt0jXEttlmm2hsbIyIiJdffjlaW1s7dCgAAAAA6CibdIbY3/zN38SoUaNi++23j0KhECNHjoxu3bqt99iXXnqppAMCAAAAQCltUhC75ppr4thjj40XXnghTjvttPiHf/iHqKmp6ejZAAAAAKDkNvlbJseOHRsREfPnz4/JkycLYgAAAAB0SpscxNa64YYbOmIOAAAAANgsNumi+gAAAADQVQhiAAAAAGRFEAMAAAAgK4IYAAAAAFkRxAAAAADIiiAGAAAAQFYEMQAAAACyIogBAAAAkBVBDAAAAICsCGIAAAAAZEUQAwAAACArghgAAAAAWRHEAAAAAMiKIAYAAABAVgQxAAAAALIiiAEAAACQFUEMAAAAgKwIYgAAAABkRRADAAAAICuCGAAAAABZEcQAAAAAyIogBgAAAEBWBDEAAAAAsiKIAQAAAJAVQQwAAACArAhiAAAAAGRFEAMAAAAgK4IYAAAAAFkRxAAAAADIiiAGAAAAQFYEMQAAAACyIogBAAAAkBVBDAAAAICsCGIAAAAAZEUQAwAAACArghgAAAAAWRHEAAAAAMiKIAYAAABAVgQxAAAAALIiiAEA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jh2bGhoa0iOPPJIeeeSR1NDQkL7xjW9s1tfLxj322GNpp512SnvvvXeaPHlycbs1kIe33347DR48OJ144onpd7/7XWpsbEyzZs1KL7zwQvEYa6Hr+9GPfpT69OmT7rzzztTY2Jh+/etfp6233jpddtllxWOsg67n7rvvTueee2669dZbU0Sk2267rc3+zfWer169OjU0NKQxY8akBQsWpJkzZ6b6+vo0adKkDv93wMbXwbvvvpu+9rWvpVtuuSU988wzad68eWnfffdNI0aMaPMY1kHX8Gm/E9a67bbb0rBhw1J9fX269NJL2+yzFjq/T1sHL7zwQurdu3eaOnVqWrBgQXrxxRfTnXfemd58883iMdYB69Npg9hf//Vfp1NOOaXNtqFDh6azzz67TBNRSsuXL08RkR588MGUUkqtra1pwIAB6aKLLioe89FHH6W6uro0ffr0lNLHfyB179493XzzzcVjXn/99VRRUZHuueeelFJKTz31VIqI9OijjxaPmTdvXoqI9Mwzz2yOl8anWLFiRdptt93SzJkz06hRo4pBzBrIx7Rp09KBBx64wf3WQh6OOOKIdPLJJ7fZduyxx6bvfve7KSXrIAef/I+ezfme33333amioiK9/vrrxWN++ctfpurq6tTU1NQhr5f121gEWeuxxx5LEVH8H+PWQde0obXw2muvpR122CEtXrw4DR48uE0Qsxa6nvWtg+OOO67498H6WAdsSKf8yOSqVati/vz5ccghh7TZfsghh8QjjzxSpqkopaampoiI6N27d0RENDY2xrJly9q859XV1TFq1Kjiez5//vxoaWlpc0x9fX00NDQUj5k3b17U1dXFvvvuWzxmv/32i7q6OmtnC/HP//zPccQRR8TXvva1NtutgXzccccdMXLkyPi7v/u76NevXwwfPjyuvfba4n5rIQ8HHnhgzJ49O5577rmIiPjDH/4QDz/8cBx++OERYR3kaHO+5/PmzYuGhoaor68vHnPooYfGypUr23x8my1DU1NTFAqF2GabbSLCOshJa2trjB8/PqZOnRp77rnnOvutha6vtbU17rrrrvjCF74Qhx56aPTr1y/23XffNh+rtA7YkE4ZxP785z/HmjVron///m229+/fP5YtW1amqSiVlFKcccYZceCBB0ZDQ0NERPF93dh7vmzZsqiqqoptt912o8f069dvnefs16+ftbMFuPnmm2PBggVx4YUXrrPPGsjHSy+9FFdffXXstttuce+998Ypp5wSp512Wtx0000RYS3kYtq0aXH88cfH0KFDo3v37jF8+PCYMmVKHH/88RFhHeRoc77ny5YtW+d5tt1226iqqrIutjAfffRRnH322fGd73wnamtrI8I6yMnFF18clZWVcdppp613v7XQ9S1fvjzee++9uOiii2Ls2LFx3333xTHHHBPHHntsPPjggxFhHbBhleUe4PMoFAptbqeU1tlG5zNp0qR44okn4uGHH15n32d5zz95zPqOt3bK79VXX43JkyfHfffdFz169NjgcdZA19fa2hojR46Mn/zkJxERMXz48PjjH/8YV199dZxwwgnF46yFru2WW26Jn/3sZ/GLX/wi9txzz1i0aFFMmTIl6uvrY8KECcXjrIP8bK733LrY8rW0tMS3v/3taG1tjauuuupTj7cOupb58+fH5ZdfHgsWLGj3+2EtdB1rv2znm9/8Zpx++ukREfHFL34xHnnkkZg+fXqMGjVqg/e1DuiUZ4j17ds3unXrtk6FXb58+TrFls7l1FNPjTvuuCPmzJkTO+64Y3H7gAEDIiI2+p4PGDAgVq1aFe+8885Gj3nzzTfXed4//elP1k6ZzZ8/P5YvXx4jRoyIysrKqKysjAcffDCuuOKKqKysLL4/1kDXt/3228cee+zRZtvuu+9e/KYgvw/yMHXq1Dj77LPj29/+duy1114xfvz4OP3004tnkFoH+dmc7/mAAQPWeZ533nknWlparIstREtLS3zrW9+KxsbGmDlzZvHssAjrIBcPPfRQLF++PAYNGlT82/GVV16JM888M3baaaeIsBZy0Ldv36isrPzUvx2tA9anUwaxqqqqGDFiRMycObPN9pkzZ8YBBxxQpqn4PFJKMWnSpJgxY0bcf//9MWTIkDb7hwwZEgMGDGjznq9atSoefPDB4ns+YsSI6N69e5tjli5dGosXLy4es//++0dTU1M89thjxWN+97vfRVNTk7VTZgcffHA8+eSTsWjRouLPyJEjY9y4cbFo0aLYeeedrYFMfPnLX45nn322zbbnnnsuBg8eHBF+H+Tigw8+iIqKtn+mdOvWrfh/gq2D/GzO93z//fePxYsXx9KlS4vH3HfffVFdXR0jRozo0NfJp1sbw55//vmYNWtW9OnTp81+6yAP48ePjyeeeKLN34719fUxderUuPfeeyPCWshBVVVV7LPPPhv929E6YIM2z7X7S+/mm29O3bt3T9dff3166qmn0pQpU1KvXr3Syy+/XO7R+Ay+//3vp7q6uvTAAw+kpUuXFn8++OCD4jEXXXRRqqurSzNmzEhPPvlkOv7449f7Ves77rhjmjVrVlqwYEE66KCD1vt1unvvvXeaN29emjdvXtprr73afJ0uW46//JbJlKyBXDz22GOpsrIy/fjHP07PP/98+vnPf5622mqr9LOf/ax4jLXQ9U2YMCHtsMMO6c4770yNjY1pxowZqW/fvumss84qHmMddD0rVqxICxcuTAsXLkwRkS655JK0cOHC4rcHbq73fPXq1amhoSEdfPDBacGCBWnWrFlpxx13TJMmTdp8/zIytrF10NLSko466qi04447pkWLFrX5u3HlypXFx7AOuoZP+53wSZ/8lsmUrIWu4NPWwYwZM1L37t3TNddck55//vn0n//5n6lbt27poYceKj6GdcD6dNogllJKP/3pT9PgwYNTVVVV+tKXvpQefPDBco/EZxQR6/254YYbise0tram888/Pw0YMCBVV1enr371q+nJJ59s8zgffvhhmjRpUurdu3fq2bNn+sY3vpGWLFnS5pi33norjRs3LtXU1KSampo0bty49M4772yGV0l7fTKIWQP5+M1vfpMaGhpSdXV1Gjp0aLrmmmva7LcWur7m5uY0efLkNGjQoNSjR4+08847p3PPPbfNf/BaB13PnDlz1vv3wIQJE1JKm/c9f+WVV9IRRxyRevbsmXr37p0mTZqUPvroo458+fw/G1sHjY2NG/y7cc6cOcXHsA66hk/7nfBJ6wti1kLntynr4Prrr0+77rpr6tGjRxo2bFi6/fbb2zyGdcD6FFJKqWPPQQMAAACALUenvIYYAAAAAHxWghgAAAAAWRHEAAAAAMiKIAYAAABAVgQxAAAAALIiiAEAAACQFUEMAAAAgKwIYgAAAABkRRADAMjcyy+/HIVCIRYtWlTuUQAANgtBDAAAAICsCGIAAGXW2toaF198cey6665RXV0dgwYNih//+McREfHkk0/GQQcdFD179ow+ffrEP/7jP8Z7771XvO/o0aNjypQpbR7v6KOPjhNPPLF4e6eddoqf/OQncfLJJ0dNTU0MGjQorrnmmuL+IUOGRETE8OHDo1AoxOjRozvstQIAbAkEMQCAMjvnnHPi4osvjvPOOy+eeuqp+MUvfhH9+/ePDz74IMaOHRvbbrtt/P73v49f//rXMWvWrJg0aVK7n+M//uM/YuTIkbFw4cKYOHFifP/7349nnnkmIiIee+yxiIiYNWtWLF26NGbMmFHS1wcAsKWpLPcAAAA5W7FiRVx++eVx5ZVXxoQJEyIiYpdddokDDzwwrr322vjwww/jpptuil69ekVExJVXXhlHHnlkXHzxxdG/f/9Nfp7DDz88Jk6cGBER06ZNi0svvTQeeOCBGDp0aGy33XYREdGnT58YMGBAiV8hAMCWxxliAABl9PTTT8fKlSvj4IMPXu++YcOGFWNYRMSXv/zlaG1tjWeffbZdz7P33nsX/7lQKMSAAQNi+fLln31wAIBOTBADACijnj17bnBfSikKhcJ6963dXlFRESmlNvtaWlrWOb579+7r3L+1tbW94wIAdAmCGABAGe22227Rs2fPmD179jr79thjj1i0aFG8//77xW2//e1vo6KiIr7whS9ERMR2220XS5cuLe5fs2ZNLF68uF0zVFVVFe8LAJADQQwAoIx69OgR06ZNi7POOituuummePHFF+PRRx+N66+/PsaNGxc9evSICRMmxOLFi2POnDlx6qmnxvjx44vXDzvooIPirrvuirvuuiueeeaZmDhxYrz77rvtmqFfv37Rs2fPuOeee+LNN9+MpqamDnilAABbDkEMAKDMzjvvvDjzzDPjhz/8Yey+++5x3HHHxfLly2OrrbaKe++9N95+++3YZ5994m//9m/j4IMPjiuvvLJ435NPPjkmTJgQJ5xwQowaNSqGDBkSY8aMadfzV1ZWxhVXXBH/9V//FfX19fHNb36z1C8RAGCLUkifvOgEAAAAAHRhzhADAAAAICuCGAAAAABZEcQAAAAAyIogBgAAAEBWBDEAAAAAsiKIAQAAAJAVQQwAAACArAhiAAAAAGRFEAMAAAAgK4IYAAAAAFkRxAAAAADIiiAGAAAAQFb+L0tNZM2zDIX9AAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 1500x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(15,5))\n",
    "sns.countplot(y='fraudulent',data=df)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 48,
   "id": "a9bc6860-b1f0-4e73-889e-35b41615c770",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "fraudulent\n",
       "0    17014\n",
       "1      866\n",
       "Name: fraudulent, dtype: int64"
      ]
     },
     "execution_count": 48,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.groupby('fraudulent')['fraudulent'].count()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 54,
   "id": "92526535-e957-48d0-9401-3ef8f6d559ca",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "{'Mid-Senior level': 3809,\n",
       " 'Entry level': 2697,\n",
       " 'Associate': 2297,\n",
       " 'Not Applicable': 1116,\n",
       " 'Director': 389,\n",
       " 'Internship': 381,\n",
       " 'Executive': 141}"
      ]
     },
     "execution_count": 54,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "exp = dict(df.required_experience.value_counts())\n",
    "del exp['']\n",
    "exp"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "id": "0833409f-95a9-479e-96e2-6bc3cb4939b3",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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mC0iokIm6ziiz2mRIyIiovzBsEVEVMi8efNG+llxo1kiIiL68jhmi4iokLh+/Tp0dHSwceNGaVnWe00RERHRl8WwRURUCMjlcjg5OSEhIUFa1qpVK6WZ6YiIiOjLYtgiIioE3rx5g9KlSyM1NRWGhoZo27ZtjtNOExER0ZfD2QiJiIiIiIhUgC1bufTPP/9ACAFdXV11F4WIiIiIiNQoLS0NMpkMDRs2/Oh2nI0wl4QQH7wpKmUnhEBqaiqfMw3F+tFsrB/NxbrRbKwfzcW60Wysn7zLbTZgy1YuKVq06tatq+aSFAyJiYkICAhArVq1ULx4cXUXh97D+tFsrB/NxbrRbKwfzcW60Wysn7y7e/durrZjyxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFqmETCaDgYEBZDKZuotCRERERKQWOuouAH0euVxAS0tzg4yBgQHMzc3VXYxc0fTnkoiIiIgKJoatAkpLS4Ylu2/gxet36i5KgVa5QklM7N9I3cUgIiIiokKIYasAe/H6HZ68jFV3MYiIiIiIKAccs0VERERERKQCDFtEREREREQqwLBFRERERESkAgxbREREREREKsCwRUREREREpAIMW0RERERERCrAsEVERERERKQCDFtEREREREQqwLBFRERERESkAgxbREREREREKsCwRUREREREpAIMW0RERERERCrAsEVERERERKQCDFtEREREREQqwLBFRERERESkAgxbREREREREKsCwRUREREREpAIMW0RERERERCrAsEVERERERKQCDFtEREREREQqwLBFRERERESkAmoJW1FRUXB1dYWVlRUaNmyI4cOH4/Hjx9L6qVOnwtTUVOlfixYtpPVyuRyrVq2CtbU16tevjyFDhiA0NFTpMQICAuDg4IAGDRqgZcuWcHNz+2LnR0REREREpJawNXLkSDx//hybN2/GwYMHoa+vj0GDBiEpKQkA8PDhQzg5OeHy5cvSv8OHD0v7r1u3Dvv27cPcuXPh4eEBmUyGYcOGITU1FQAQHR2NwYMHo3r16vD09ISzszNWrlwJT09PdZwuEREREREVQV88bEVHR6Ny5cqYM2cO6tati5o1a+LXX3/Fmzdv8OjRI2RkZODx48eoW7cujIyMpH9ly5YFAKSmpmLr1q1wdnaGjY0NzMzMsHz5crx+/RqnT58GAOzfvx96enqYNWsWatasCXt7ewwaNAibN2/+0qdLRERERERF1BcPW1999RWWLVuG7777DgAQGRkJNzc3GBsbo1atWggJCUFKSgpq1qyZ4/6BgYFISEiAlZWVtKxUqVIwNzeHn58fAMDf3x+WlpbQ0dGRtrGyskJwcDCioqJUeHZERERERESZdD69ier873//k1qh1q9fj+LFiyMoKAgymQzu7u64ePEitLS0YGNjg3HjxqFkyZIIDw8HAFSsWFHpWOXLl8erV68AAOHh4TAxMcm2HgDCwsJQrly5zyqvEAKJiYmftW9+kslkMDAwUHcxCpWkpCQIIdRdjC9G0WVX8T9pFtaP5mLdaDbWj+Zi3Wg21k/eCSEgk8k+uZ1aw9bAgQPRp08f7N27F6NGjcKePXvw6NEjaGlpoVKlStiwYQNCQ0OxaNEiBAUFwd3dXXoR6OnpKR2rWLFiiI2NBQAkJyfnuB4AUlJSPru8aWlpCAgI+Oz984uBgQHMzc3VXYxCJTg4uEh+wISEhKi7CPQRrB/NxbrRbKwfzcW60Wysn7x5P2/kRK1hq1atWgCAOXPm4NatW9i1axfmz5+PQYMGoVSpUgAAExMTGBkZoU+fPrh79y709fUBZI7dUvwMZIYoRWuPvr6+NFlG1vUAULx48c8ur66urlRmdcpNiqa8qVGjRpFr2QoJCUH16tXZSqqBWD+ai3Wj2Vg/mot1o9lYP3mXdSb1j/niYSsqKgo+Pj7o2LEjtLW1AQBaWlqoWbMmIiIiIJPJpKCloOgSGB4eLnUfjIiIQNWqVaVtIiIiYGZmBgAwNjZGRESE0jEUv1eoUOGzyy6Tyf5TWCPNVVQ/WAwMDPia1mCsH83FutFsrB/NxbrRbKyf3Mtt48cXnyAjIiICLi4uuH79urQsLS0NDx48QM2aNeHi4oKhQ4cq7XP37l0AmS1hZmZmMDQ0hK+vr7Q+Li4ODx48gIWFBQDA0tISN27cQEZGhrSNj48PatSo8dnjtYiIiIiIiPLii4ctMzMzNG/eHLNnz4a/vz+CgoIwefJkxMXFYdCgQbC1tcWVK1ewfv16PHv2DBcuXMC0adNga2uLmjVrQk9PDw4ODliyZAnOnj2LwMBAjB8/HsbGxmjXrh0AwN7eHvHx8Zg+fToeP34MLy8vuLu7Y8SIEV/6dImIiIiIqIj64t0IZTIZVqxYgaVLl2LcuHF49+4dLCwssHv3bnzzzTf45ptvsHLlSmzYsAEbNmxAyZIl0aVLF4wbN046xpgxY5Ceno4ZM2YgOTkZlpaWcHNzkwaplStXDlu2bMG8efNgZ2cHIyMjTJo0CXZ2dl/6dImIiIiIqIhSywQZJUuWxKxZszBr1qwc17dv3x7t27f/4P7a2tpwdXWFq6vrB7epV68ePDw8/mtRiYiIiIiIPssX70ZIRERERERUFDBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpgFrCVlRUFFxdXWFlZYWGDRti+PDhePz4sbQ+ICAADg4OaNCgAVq2bAk3Nzel/eVyOVatWgVra2vUr18fQ4YMQWhoqNI2nzoGERERERGRKqklbI0cORLPnz/H5s2bcfDgQejr62PQoEFISkpCdHQ0Bg8ejOrVq8PT0xPOzs5YuXIlPD09pf3XrVuHffv2Ye7cufDw8IBMJsOwYcOQmpoKALk6BhERERERkSrpfOkHjI6ORuXKlTFy5Eh89913AIBff/0V3bp1w6NHj+Dj4wM9PT3MmjULOjo6qFmzJkJDQ7F582bY29sjNTUVW7duhaurK2xsbAAAy5cvh7W1NU6fPo3OnTtj//79Hz0GERER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pAIMW0RERERERCrAsEVERERERKQCDFtEREREREQq8J/C1pMnT/D69ev8KgsREREREVGhkaewdfPmTXTv3h0AsG/fPnTu3Blt2rTBmTNnVFE2IqIiSSaTwcDAADKZTN1FISIiov9AJy8bL126FC1btoQQAhs3bsTChQtRpkwZLF26FG3btlVVGYmI8o1cLqClpdkhxsDAAObm5uouxicVhOeSiIhInfIUtp4+fYpdu3bh6dOniIyMRKdOnaCnp4fx48erqnxERPlKS0uGJbtv4MXrd+ouSoFWuUJJTOzfSN3FICIi0mh5Clva2tpISEjAxYsX0aBBA+jp6eHly5cwNDRUVfmIiPLdi9fv8ORlrLqLQURERIVcnsJW27Zt4eDggJcvX2LGjBl4/PgxRo0aBVtbW1WVj4iIiIiIqEDKU9j63//+hz///BP6+vro1KkTQkJC0LdvXwwcOFBV5SMiIiIiIiqQ8tyNsEePHnjz5g3u3buHSpUqYfDgwaoqGxERERERUYGVp7AVGRkJV1dXXLt2DUIIyGQy/PTTT5g3bx7HbREREREREWWRp/tszZ07FwYGBvj7779x584dHD16FImJiZg/f76qykdERERERFQg5ally9fXF2fOnEGJEiUAALVq1cKSJUvQoUMHlRSOiIiIiIiooMpTy9ZXX32Fd++U702TkpKCYsWK5WuhiIiIiIiICrpctWz5+fkByJz63cnJCWPHjkWlSpUQERGB1atXo2fPniotJBERERERUUGTq7Dl6Oio9PvIkSOVfr9z5w5Gjx6df6UiIiIiIiIq4HIVtgIDA1VdDiIiIiIiokIlTxNkAEB4eDiOHj2Kly9fonz58rC1tUXVqlVVUTYiIiIiIqICK08TZNy9exedO3fGqVOnEBsbi7Nnz6Jr1664ceOGqspHRERERERUIOWpZWvx4sUYO3YsBgwYIC1zd3fHkiVLsHfv3nwvHBERERERUUGVp5athw8fol+/fkrL+vXrh6CgoHwtFBERERERUUGXp7BlYGCAV69eKS179eoVSpcuna+FIiIiIiIiKujyFLY6deoEZ2dnXLp0CcHBwbhw4QLGjBmDTp06qap8REREREREBVKexmyNHTsWb9++xa+//oq0tDQUK1YM9vb2vMcWERERERHRe/IUtooVK4aFCxfi999/R2xsLL7++mvIZDJVlY2I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REQFVZ4myJg4cSIcHR1x5MgRVKpUCS9fvoRMJsO2bdtUVT4iIiIiIqICKU9hy8TEBCdPnsSZM2fw9u1bVKpUCTY2NjA0NFRV+YiIiIiIiAqkPIUtAChTpgx69uypirIQEREREREVGrkKW61bt4ZMJvvgeplMxhkJiYiIiIiIsshV2HJ2ds5x+a1bt+Dh4QFzc/N8LRQREREREVFBl6uwZWdnl23Z1q1b4enpiZ9//hlTp07N94IREREREREVZHkesxUXF4fJkyfD398fixcvRseOHVVRLiIiIiIiogItT2Hr1q1bGD9+PL766it4eXmhSpUqqioXERERERFRgZbrmxpv2bIFjo6OaNOmDfbt28egRURERERE9BG5atlycnLChQsX4ODggJ9++gm3b9/Oto2lpWW+F46IiIiIiKigylXY8vb2BgDs3LkTO3fuzLZeJpMhICAgXwtGRERERERUkOUqbAUGBqq6HERERERERIVKrsdsERERERERUe4xbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCqg9bK1btw6Ojo5Ky6ZOnQpTU1Olfy1atJDWy+VyrFq1CtbW1qhfvz6GDBmC0NBQpWMEBATAwcEBDRo0QMuWLeHm5vZFzoeIiIiIiAhQc9javn07Vq1alW35w4cP4eTkhMuXL0v/Dh8+LK1ft24d9u3bh7lz58LDwwMymQzDhg1DamoqACA6OhqDBw9G9erV4enpCWdnZ6xcuRKenp5f6tSIiIiIiKiI01HHg75+/RrTp0/HjRs3UKNGDaV1GRkZePz4MX799VcYGRll2zc1NRVbt26Fq6srbGxsAADLly+HtbU1Tp8+jc6dO2P//v3Q09PDrFmzoKOjg5o1ayI0NBSbN2+Gvb39FzlHIiIiIiIq2tTSsnX//n2ULl0aR44cQf369ZXWhYSEICUlBTVr1sxx38DAQCQkJMDKykpaVqpUKZibm8PPzw8A4O/vD0tLS+jo/JslraysEBwcjKioKBWcERERERERkTK1tGy1bt0arVu3znFdUFAQZDIZ3N3dcfHiRWhpacHGxgbjxo1DyZIlER4eDgCoWLGi0n7ly5fHq1evAADh4eEw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sEaaix8smot1o9lYP5qtqNaPgYEB/15rKNaNZmP95F5uvyBU+3223mdpaYkbN24gIyNDWubj44MaNWqgXLlyMDMzg6GhIXx9faX1cXFxePDgASwsLHJ1DCIiIiIiIlXTuLBlb2+P+Ph4TJ8+HY8fP4aXlxfc3d0xYsQIAJl9Ix0cHLBkyRKcPXsWgYGBGD9+PIyNjdGuXbtcHYOIiIiIiEjVNK4bYbly5bBlyxbMmzcPdnZ2MDIywqRJk2BnZydtM2bMGKSnp2PGjBlITk6GpaUl3NzcpEFquTkGERERERGRKqk9bC1cuDDbsnr16sHDw+OD+2hra8PV1RWurq4f3OZTxyAiIiIiIlIljetGSEREREREVBgwbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqYDGhq2XL1/C1NQ0278DBw4AAAICAuDg4IAGDRqgZcuWcHNzU9pfLpdj1apVsLa2Rv369TFkyBCEhoaq41SIiIiIiKgI0lF3AT7k4cOHKFasGM6cOQOZTCYtL1myJKKjozF48GC0bdsWs2fPxq1btzB79myUKVMG9vb2AIB169Zh3759WLBgASpUqIDFixdj2LBhOHbsGPT09NR1WkREREREVERobNgKCgpCjRo1UL58+Wzr3N3doaenh1mzZkFHRwc1a9ZEaGgoNm/eDHt7e6SmpmLr1q1wdXWFjY0NAGD58uWwtrbG6dOn0blz5y99OkREREREVMRobDfChw8folatWjmu8/f3h6WlJXR0/s2KVlZWCA4ORlRUFAIDA5GQkAArKytpfalSpWBubg4/Pz+Vl52IiIiIiEijW7aMjIzQr18/hISEoFq1avj1119hbW2N8PBwmJiYKG2vaAELCwtDeHg4AKBixYrZtnn16tVnl0kIgcTExM/eP7/IZDIYGBiouxiFSlJSEoQQ+XIs1k/+Yt1oNtaPZsvP+ikIkpKSlP4nzcG60Wysn7wTQigNdfoQjQxbqampCAkJgYGBASZNmoTixYvjyJEjGDZsGLZt24bk5ORs466KFSsGAEhJSZFeKDltExsb+9nlSktLQ0BAwGfvn18MDAxgbm6u7mIUKsHBwfn2AcP6yV+sG83G+tFs+Vk/BUlISIi6i0AfwLrRbKyfvMnNPBAaGbb09PTg5+cHHR0d6STq1KmDJ0+ewM3NDfr6+khNTVXaJyUlBQBQvHhx6OvrA8gMbYqfFdv8l29NdXV1P9i18UvKTYqmvKlRo0a+fjtP+Yd1o9lYP5otP+unIEhKSkJISAiqV6/OVlINw7rRbKyfvHv8+HGuttPIsAVkhqb3mZiY4PLlyzA2NkZERITSOsXvFSpUQHp6urSsatWqStuYmZl9dplkMlmO5aKCjx8smot1o9lYP5qtqNaPgYEB/15rKNaNZmP95F5uvyDUyAkyAgMD0bBhQ/j7+ystv3fvHmrVqgVLS0vcuHEDGRkZ0jofHx/UqFED5cqVg5mZGQwNDeHr6yutj4uLw4MHD2BhYfHFzoOIiIiIiIoujQxbJiYm+O677zB79mz4+/vjyZMnWLBgAW7dugUnJyfY29sjPj4e06dPx+PHj+Hl5QV3d3eMGDECQGY3RAcHByxZsgRnz55FYGAgxo8fD2NjY7Rr107NZ0dEREREREWBRnYj1NLSwoYNG7BkyRKMGzcOcXFxMDc3x7Zt22BqagoA2LJlC+bNmwc7OzsYGRlh0qRJsLOzk44xZswYpKenY8aMGUhOToalpSXc3Nx4Q2MiIiIiIvoiNDJsAUDZsmUxf/78D66vV68ePDw8PrheW1sbrq6ucHV1VUXxiIiIiIiIPkojuxESEREREREVdAxbREREREREKsCwRUREREREpAIMW0RERFQoyGQyGBgY8AbZRKQxNHaCDCIiItIccrmAlpZmhxgDAwOYm5uruxifVBCey/zGIExFFcMWERERfZKWlgxLdt/Ai9fv1F2UAq1yhZKY2L9Rvh9X0wNcQQnCgOY/l1SwMGwRERFRrrx4/Q5PXsaquxiUA4bh/KGqMExFF8MWERERUSHAMEykeThBBhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBEREREREakAwxYREREREZEKMGwRERERERGpAMMWERERERGRCjBsERERERERqQDDFhERERERkQowbBERERERFWEymQwGBgaQyWTqLkqho6PuAhARERERFWZyuYCWluYGGQMDA5ibm6u7GLmi6c/l+xi2iIiIiIhUSEtLhiW7b+DF63fqLkqBVrlCSUzs30jdxcgThi0iIiIiIhV78fodnryMVXcx6AvjmC0iIiIiIiIVYNgiIiIiIiJSAYYtIiIiIiIiFWDYIiIiIiIiUgGGLSIiIiIiIhUo1GFLLpdj1apVsLa2Rv369TFkyBCEhoaqu1hERERERFQEFOqwtW7dOuzbtw9z586Fh4cHZDIZhg0bhtTUVHUXjYiIiIiICrlCG7ZSU1OxdetWODs7w8bGBmZmZli+fDlev36N06dPq7t4RERERERUyBXasBUYGIiEhARYWVlJy0qVKgVzc3P4+fmpsWRERERERFQUyIQQQt2FUIVTp07B2dkZt2/fhr6+vrR87NixSE5OxsaNG/N0vJs3b0IIAV1d3fwu6meRyWSIjU9FeoZc3UUp0HS0tVDaUA/5/TZg/fx3rBvNxvrRbKqoH9ZN/uB7R7OxfjSbqurnc6SlpUEmk+GHH3746HY6X6g8X1xSUhIAQE9PT2l5sWLFEBsbm+fjyWQypf81QWlDvU9vRLmiinpl/eQP1o1mY/1otvyuH9ZN/uF7R7OxfjSbJlyPy2SyXJWj0IYtRWtWamqqUstWSkoKDAwM8ny8hg0b5lvZiIiIiIio8Cu0Y7YqVqwIAIiIiFBaHhERAWNjY3UUiYiIiIiIipBCG7bMzMxgaGgIX19faVlcXBwePHgACwsLNZaMiIiIiIiKgkLbjVBPTw8ODg5YsmQJypYti0qVKmHx4sUwNjZGu3bt1F08IiIiIiIq5Apt2AKAMWPGID09HTNmzEBycjIsLS3h5uaWbdIMIiIiIiKi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",
      "text/plain": [
       "<Figure size 1000x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "plt.figure(figsize=(10,5))\n",
    "sns.set_theme(style=\"whitegrid\")\n",
    "plt.bar(exp.keys(),exp.values())\n",
    "plt.title('No of jobs with experience',size=20)\n",
    "plt.xlabel('Experience',size=10)\n",
    "plt.ylabel('No of jobs',size=10)\n",
    "plt.xticks(rotation=30)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "id": "da8e333f-e0b8-4f4f-af89-48a4a5a732e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "def split(location):\n",
    "    l =  location.split(',')\n",
    "    return l[0]\n",
    "df['country']=df.location.apply(split)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91655aca-c570-4057-9e08-e49725978fcd",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b5a9147c-9b85-4bb9-bc6e-2f5465696c70",
   "metadata": {},
   "outputs": [],
   "source": [
    "countr= dict(df.country.value_counts()[:14])\n",
    "del countr['']\n",
    "countr"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "30198bce-7205-43b4-9e84-adce455af25f",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "plt.figure(figsize=(8,6))\n",
    "plt.title('Country-wise job posting',size=20)\n",
    "plt.bar(countr.keys(),countr.values())\n",
    "plt.ylabel('No of jobs',size=10)\n",
    "plt.xlabel('Countries',size=10)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a3caa52d-cb59-473d-b435-7f85f6fa9ec2",
   "metadata": {},
   "outputs": [],
   "source": [
    "edu = dict(df.required_education.value_counts()[:7])\n",
    "del edu[' ']\n",
    "edu"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ec2a1667-9bcf-428b-92e2-32a35b077e2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(df[df.fraudulent==0].title.value_counts()[:10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "91f5ca13-31e3-4b6e-bda3-f6b59ba4676f",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(df[df.fraudulent==1 ].title.value_counts()[:10])"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63dd6a1a-0ee8-469d-8194-e85d4e4938d2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['text']=df['title']+' '+df['company_profile']+' '+df['description']+' '+df['requirements']+' '+df['benefits']\n",
    "del df['title']\n",
    "del df['location']\n",
    "del df['department']\n",
    "del df['company_profile']\n",
    "del df['description']\n",
    "del df['requirements']\n",
    "del df['benefits']\n",
    "del df['required_experience']\n",
    "del df['required_education']\n",
    "del df['industry']\n",
    "del df['function']\n",
    "del df['country']"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c4bd916-851f-4d68-9403-f4887f0f01ed",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58ac67e2-3ee9-45b6-b610-0af70a17879c",
   "metadata": {},
   "outputs": [],
   "source": [
    "fraudjobs_text = df[df.fraudulent==1].text\n",
    "realjobs_text = df[df.fraudulent==0].text-"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0beeec8b-adc0-44cb-8643-6cdddf33fe63",
   "metadata": {},
   "outputs": [],
   "source": [
    "STOPWORDS = spacy.lang.en.stop_words.STOP_WORDS\n",
    "plt.figure(figsize = (16,14))\n",
    "wc = WordCloud(min_font_size = 3, max_words = 3000 , width = 1600 , height = 800 , stopwords = STOPWORDS).generate(str(\" \".join(fraudjobs_text)))\n",
    "plt.imshow(wc,interpolation = 'bilinear')            "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f2d13c8c-2e99-4dba-ae36-92694a98a299",
   "metadata": {},
   "outputs": [],
   "source": [
    "STOPWORDS = spacy.lang.en.stop_words.STOP_WORDS\n",
    "plt.figure(figsize = (16,14))\n",
    "wc = WordCloud(min_font_size = 3, max_words = 3000 , width = 1600 , height = 800 , stopwords = STOPWORDS).generate(str(\" \".join(realjobs_text)))\n",
    "plt.imshow(wc,interpolation = 'bilinear')            \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1f123d81-778f-4d4b-9330-397a134a259f",
   "metadata": {},
   "outputs": [],
   "source": [
    "!pip install spacy && python  -m spacy download en"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "042b3b47-42bf-43c3-bb40-27244920cbf8",
   "metadata": {},
   "outputs": [],
   "source": [
    "punctuations = string.punctuation\n",
    "\n",
    "nlp = spacy.load(\"en_core_web_sm\")\n",
    "stop_words = spacy.lang.en.stop_words.STOP_WORDS\n",
    "\n",
    "parser = English()\n",
    "\n",
    "def spacy_tokenizer(sentence):\n",
    "    mytokens = [word.lemma_.lower().strip() if word.lemma_ != \"-PRON-\" else word.lower_for word in mytokens ]\n",
    "\n",
    "    mytockens = [word for word in mytokens if word not in stop_words and word not in punctuations ]\n",
    "\n",
    "    return mytokens\n",
    "\n",
    "class predictors(TransformerMixin):\n",
    "    def transform(self, X, **transform_params):\n",
    "\n",
    "        return[clean_text(text) for text in X]\n",
    "\n",
    "    def fit(self, X, y=None, **fit_params):\n",
    "        return self\n",
    "\n",
    "    def get_params(self, deep=True):\n",
    "        return {}\n",
    "\n",
    "def clean_text(text):\n",
    "    return text.strip().lower()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6d7b919a-d0e4-43c0-99ca-b7f34be1da14",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['text'] = df['text'].apply(clean_text)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "95ee9dd2-53ee-4028-b3fd-8d82abcad994",
   "metadata": {},
   "outputs": [],
   "source": [
    "cv = TfidfVectorizer(max_features = 100)\n",
    "x=cv.fit_transform(df['text'])\n",
    "df1 = pd.DataFrame(x.toarray(), columns=cv.get_feature_names())\n",
    "df.drop([\"text\"], axis=1, inplace=True)\n",
    "main_df = pd.concat([df1,df], axis =1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8e97d4db-3653-4d49-9838-063ad0f62da7",
   "metadata": {},
   "outputs": [],
   "source": [
    "main_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "9f7170c1-ea34-4926-9dcd-3bf778dd8e79",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'main_df' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[7], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m Y \u001b[38;5;241m=\u001b[39m main_df\u001b[38;5;241m.\u001b[39miloc[:,\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m1\u001b[39m]\n\u001b[0;32m      2\u001b[0m X \u001b[38;5;241m=\u001b[39m main_df\u001b[38;5;241m.\u001b[39miloc[ :,:\u001b[38;5;241m-\u001b[39m\u001b[38;5;241m1\u001b[39m]\n\u001b[0;32m      4\u001b[0m X_train, X_test, y_train, y_test \u001b[38;5;241m=\u001b[39m train_test_split(X,Y, test_size\u001b[38;5;241m=\u001b[39m\u001b[38;5;241m0.3\u001b[39m)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'main_df' is not defined"
     ]
    }
   ],
   "source": [
    "Y = main_df.iloc[:,-1]\n",
    "X = main_df.iloc[ :,:-1]\n",
    "\n",
    "X_train, X_test, y_train, y_test = train_test_split(X,Y, test_size=0.3)\n",
    "\n",
    "print(X_train.shape)\n",
    "print(y_train.shape)\n",
    "print(X_test.shape)\n",
    "print(y_test.shape)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8df8d1f0-22ef-476c-beb2-7b3571c743e6",
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.ensemble import RandomForestClassifier\n",
    "rfc = RandomForestClassifier(n_jobs=3,oob_score=True,n_estimators=100,criterion=\"entropy\")\n",
    "model=rfc.fit(X_train,y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "80da9e50-8416-418b-92ec-85d46d9382b6",
   "metadata": {},
   "outputs": [
    {
     "ename": "NameError",
     "evalue": "name 'X_test' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[9], line 1\u001b[0m\n\u001b[1;32m----> 1\u001b[0m \u001b[38;5;28mprint\u001b[39m(X_test)\n",
      "\u001b[1;31mNameError\u001b[0m: name 'X_test' is not defined"
     ]
    }
   ],
   "source": [
    "print(X_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2e6b3e92-6831-489f-99f1-e5805c498bfb",
   "metadata": {},
   "outputs": [],
   "source": [
    "pred = rfc.predict(X_test)\n",
    "score = accuracy_score(y_test,pred)\n",
    "score"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "778915cc-5125-42c4-baad-3847536e12e7",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Classification report\n",
      "\n"
     ]
    },
    {
     "ename": "NameError",
     "evalue": "name 'classification_report' is not defined",
     "output_type": "error",
     "traceback": [
      "\u001b[1;31m---------------------------------------------------------------------------\u001b[0m",
      "\u001b[1;31mNameError\u001b[0m                                 Traceback (most recent call last)",
      "Cell \u001b[1;32mIn[11], line 2\u001b[0m\n\u001b[0;32m      1\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mClassification report\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[1;32m----> 2\u001b[0m \u001b[38;5;28mprint\u001b[39m(classification_report(y_test,pred))\n\u001b[0;32m      3\u001b[0m \u001b[38;5;28mprint\u001b[39m(\u001b[38;5;124m\"\u001b[39m\u001b[38;5;124mConfusion Matrix\u001b[39m\u001b[38;5;130;01m\\n\u001b[39;00m\u001b[38;5;124m\"\u001b[39m)\n\u001b[0;32m      4\u001b[0m \u001b[38;5;28mprint\u001b[39m(confusion_matrix(y_test,pred))\n",
      "\u001b[1;31mNameError\u001b[0m: name 'classification_report' is not defined"
     ]
    }
   ],
   "source": [
    "print(\"Classification report\\n\")\n",
    "print(classification_report(y_test,pred))\n",
    "print(\"Confusion Matrix\\n\")\n",
    "print(confusion_matrix(y_test,pred))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "98afba9e-0a5e-47eb-b642-205a5d5e3200",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f4ca9068-23ea-4700-b2eb-143d6871827b",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a5d68fa3-bec5-4096-a57a-fdba7bae31fc",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
