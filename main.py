from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

# Importing relevant libraries

bot = ChatBot(  # Creating a chat bot object
    "Breast_Cancer_Chat_Bot",  # Naming the chatbot object
    logic_adapters = [  # Specifying the logic adapter of the chat bot. This determines how the chatbot selects its responses to user inputs.
        {
            'import_path': 'chatterbot.logic.BestMatch',
            'default_response': 'I am sorry, I do not know how to respond.', # Specify response to give when no good match is found.
            'maximum_similarity_threshold': 0.90
        }
    ]
)

bot.storage.drop()  # clear all past training
trainer = ChatterBotCorpusTrainer(bot)  # create a trainer object for corpus training
trainer.train("chatterbot.corpus.english")  # Use the trainer object to train the bot using the English corpus

knowledgeBase = [  # Creating a knowledge base of breast cancer facts.
    "What is cancer?",
    "Cancer is a disease caused by the growth of abnormal malignant cells (usually in the form of tumors) in the body. Cancer can occur in various parts of the body. ",

    "What is breast cancer?",
    "A disease characterized by the growth of malignant cells in the milk glands or ducts of human breasts. ",

    "Can males get breast cancer?",
    "Breast cancer can strike males and females, although women are about 100 times more likely to develop the disease than men.",

    "At what age can you get breast cancer?",
    "Most cancers in female breasts form shortly before, during, or after menopause, with three-quarters of all cases being diagnosed after age 50.",

    "Do we know what causes breast cancer?",
    "No. The exact causes of breast cancer are largely unknown, but both environmental and genetic factors are involved.",

    "What are the genetic risk factors for breast cancer?",
    "Specific mutations in genes called HER2, BRCA1, BRCA2, CHEK2, and p53 have been linked to breast cancer; these mutations may be inherited or acquired.",

    "What are the environmental risk factors for breast cancer?",
    "For all women, lack of exercise, obesity, use of oral contraceptives, alcohol consumption, smoking, and previous medical treatments involving chest irradiation are considered risk factors for breast cancer. ",

    "What are the symptoms of breast cancer?",
    "The most common symptoms are: swelling of the breast, a lump in the breast, a lump beside the breast, or a lump under the arm. ",

    "What are other possible symptoms of breast cancer?",
    "Other symptoms may include unexplained breast pain, abnormal nipple discharge, changes in breast texture, or changes in the skin on or around the breast.",

    "How is breast cancer diagnosed?",
    "Breast cancer is typically diagnosed through physical (self) examination, mammography and/or biopsy.",

    "What is a mammography?",
    "Mammography entails the use of X-rays to detect lesions in breast tissue. Mammography is often used for initial diagnosis, but, in order to confirm the presence of cancer, a tissue sample (biopsy) usually must be taken.",

    "What is a biopsy?",
    "A biopsy is a medical procedure where a sample of tissue is taken (in this case, from a tumor) and examined to diagnose a disease.",

    "What is it called when breast cancer spreads?",
    "Metastasis."

    "How does breast cancer spread?",
    "Metastasis generally begins in a so-called sentinel lymph node (the first lymph node invaded by cancer cells) and, in the case of breast cancer, spreads to axillary lymph nodes, which are located in and around the armpits.",

    "How does breast cancer metastasize?",
    "Metastasis generally begins in a so-called sentinel lymph node (the first lymph node invaded by cancer cells) and, in the case of breast cancer, spreads to axillary lymph nodes, which are located in and around the armpits.",

    "How can we tell how far cancer has spread?",
    "Several imaging methods may be used to determine the degree of metastasis, including X-rays, computerized axial tomography (CAT) scans, or magnetic resonance imaging (MRI). The presence of receptors for the hormones estrogen and progesterone is also determined because these receptors play an important role in the cancer’s development and in decisions regarding the appropriate treatment.",

    "How can we tell how far cancer has metastasized?",
    "Several imaging methods may be used to determine the degree of metastasis, including X-rays, computerized axial tomography (CAT) scans, or magnetic resonance imaging (MRI). The presence of receptors for the hormones estrogen and progesterone is also determined because these receptors play an important role in the cancer’s development and in decisions regarding the appropriate treatment.",

    "Are there different types of breast cancer?",
    "Yes."

    "How many different types of breast cancer are there?",
    "There are at least 2 main categories of breast cancer. But there are multiple ways to classify breast tumours.",

    "Where do the different types of breast cancer come from?",
    "Types of breast cancer are created according to the glandular tissue the cancer originates from, its outward appearance, its cellular composition, its cellular origin, and its activity."

    "What types of breast cancer are there?",
    "Almost all cases of breast cancer begin in the glandular tissues that either produce milk (lobular tissue) or provide a passage for milk (ductal tissue) to the nipple. Cancers of these tissues are called lobular carcinomas and ductal carcinomas.",

    "Which type of breast cancer is most common?",
    "The most common type of tumour, called infiltrating ductal carcinoma, is a single, hard, barely movable lump. This type of tumour accounts for about 70 percent of all cases. Fewer than 15 percent of all cases are lobular carcinomas.",

    "How is breast cancer treated?",
    "Treatment may entail surgery, radiation, or chemotherapy. Biological treatment is also an option.",

    "What is the best first course of treatment?",
    "It depends, but surgery is ususally the first step.",

    "What is surgery?",
    "Surgical treatments of breast cancer seek to remove the tumours.",

    "Are there different kinds of surgery?",
    "Yes.",

    "What are the different kinds of surgery?",
    "There are many different kinds of relevant surgeries, including: lumpectomy, simple mastectomy, radical mastectomy, and modified radical mastectomy.",

    "What is a lumpectomy?",
    "A lumpectomy removes only the cancerous mass and a small amount of surrounding tissue.",

    "What is a simple mastectomy?",
    "A simple mastectomy removes the entire breast. (EB)",

    "What is a radical mastectomy?",
    "Radical mastectomies involving removal of the breast, underlying muscle, and other tissue are rarely performed.",

    "What is a modified radical mastectomy?",
    "A modified radical mastectomy removes the breast along with adjacent lymph nodes.",

    "Are there risks associated with surgical treatments?",
    "Yes.",

    "What are the risks associated with surgical treatments?",
    "Surgery is associated with a wide range of side effects, including changes in arm or shoulder mobility, swelling, infection, numbness, and, when lymph nodes are removed, fluid buildup in the region they were taken from.",

    "How do patients recover from surgical treatments?",
    "Partial or complete breast removal is often followed by cosmetic or reconstructive surgery.",

    "What is radiation treatment?",
    "Radiation is usually employed—either to shrink tumours before surgery or to destroy small amounts of cancerous tissue remaining after surgery.",

    "Are there risks associated with radiation treatments?",
    "Yes.",

    "What are the risks associated with breast cancer treatments?",
    "Side effects of radiation include swelling or thickening of the breast, vomiting, fatigue, diarrhea, or skin irritations resembling sunburn.",

    "What is chemotherapy?",
    "The use of chemicals to destroy cancerous cells. (EB)",

    "Are there risks associated with chemotherapy?",
    "Yes,",

    "What are the risks assocaited with chemotherapy?",
    "Chemotherapeutic agents also attack normal cells to some degree, causing side effects that include hair loss, immune suppression, mouth sores, fatigue, and nausea.",

    "What is biological treatment?",
    "When chemical inhibitors are used to block the hormones that stimulate growth of cancer cells.",

    "What drugs are used in biological treatment?",
    "Common drugs inlcude Tamoxifen, Megace (megestrol), Herceptin, and Letrozole.",

    "What is Tamoxifen?",
    "Tamoxifen is a common drug that blocks the ability of estrogen to stimulate tumour growth.",

    "What is Megace (megestrol)?",
    "Megace (megestrol) blocks the action of progesterone by partially mimicking the hormone.",

    "What is Herceptin?",
    "Herceptin is a manufactured antibody that binds to growth factor receptors on the surface of cancer cells and thereby blocks cell proliferation.",

    "What is Letrozole?",
    "Letrozole is used to inhibit the synthesis of estrogen in postmenopausal women who have hormone-dependent breast cancers.",

    "Can breast cancer be prevented?",
    "Breast cancer cannot be completely prevented, but the risk of developing advanced disease can be greatly reduced by several means.",

    "How can one reduce their risk of breast cancer?",
    "Maintaining a healthy body weight, decreasing alcohol consumption, and ceasing to smoke can each contribute to a reduction in breast cancer risk.",

    "Are there stages of breast cancer?",
    "Yes.",

    "What do the stages of breast cancer mean?",
    "The stages range from 0-4, where higher stages indicate cancer that is more dangerous and has spread.",

    "How many stages of breast cancer are there?",
    "The stages range from 0-4, where higher stages indicate cancer that is more dangerous and has spread.",

]

trainer = ListTrainer(bot) # creating another trainer object for list (knowledge base) training
trainer.train(knowledgeBase)  # use trainer object to train bot using knowlege base

while True: # create loop that allows user to continuously interact with the bot
    try:
        user_input = input("Ask a breast cancer related question:")
        response = bot.get_response(user_input)
        print(response)

    except(KeyboardInterrupt, EOFError, SystemExit):
        break

# References for knowledge base
# Encyclopedia Britannica. (2022). breast cancer | Definition, Causes, Symptoms, & Treatment. Retrieved 27 June 2022, from https://www.britannica.com/science/breast-cancer#ref293987
# encyclopedia.com. (2022). Breast Cancer. Encyclopedia.com. Retrieved from https://www.encyclopedia.com/caregiving/encyclopedias-almanacs-transcripts-and-maps/breast-cancer
