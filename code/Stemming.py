from DataCleaning import LanguageCode, duplicatesRemoval

Gujarati_SuffixDictionary = {'ઓથી': [3, 'ી', 'થ', 'ઓ', ''], 'ઓની': [3, 'ી', 'ન', 'ઓ', ''],
                             'ઓમાં': [4, 'ં', 'ા', 'મ', 'ઓ', ''], 'ઓએ': [2, 'એ', 'ઓ', ''],
                             'માં': [3, 'ં', 'ા', 'મ', ''],
                             'માંથી': [5, 'ી', 'થ', 'ં', 'ા', 'મ', ''],
                             'નાં': [3, 'ં', 'ા', 'ન', ''],
                             'થી': [2, 'ી', 'થ', ''],
                             'ાથી': [3, 'ી', 'થ', 'ા', 'ો'], 'નું': [3, 'ં', 'ુ', 'ન', ''], 'નુ': [2, 'ુ', 'ન', ''],
                             'ની': [2, 'ી', 'ન', ''],
                             'ને': [2, 'ે', 'ન', ''],
                             'ના': [2, 'ા', 'ન', ''], 'નો': [2, 'ો', 'ન', ''], 'એ': [1, 'એ', ''], 'ઓ': [1, 'ઓ', '']}

Hindi_SuffixDictionary = {'तेर्': [4, '्', 'र', 'े', 'त', 'ना'], 'ते': [2, 'े', 'त', 'ना'], 'ओं': [2, 'ं', 'ओ', ''],
                          'यों': [3, 'ं', 'ो', 'य', ''],
                          'ों': [2, 'ं', 'ो', ''],
                          'ने': [2, 'े', 'न', 'ना'], 'े': [1, 'े', 'ा'], 'ओंर्': [4, '्', 'र', 'ं', 'ओ', ''],
                          'र्': [2, '्', 'र', ''],
                          'ता': [2, 'ा', 'त', 'ना'], 'इये': [3, 'े', 'य', 'इ', 'ओ'],
                          'ऊंगा': [4, 'ा', 'ग', 'ं', 'ऊ', 'ना'],
                          'ूंगा': [4, 'ा', 'ग', 'ं', 'ू', 'ना'],
                          'मे': [2, 'े', 'म', ''], 'में': [3, 'ं', 'े', 'म', ''], 'ः': [1, 'ः', '']}

global SuffixDictionary

if LanguageCode == 'gu':
    SuffixDictionary = Gujarati_SuffixDictionary
    FileName = 'GujaratiOutput.txt'
elif LanguageCode == 'hi':
    SuffixDictionary = Hindi_SuffixDictionary
    FileName = 'HindiOutput.txt'

KeysOfSuffixDictionary = SuffixDictionary.keys()


def stemming():
    with open(FileName, 'r', encoding='utf-8') as OR:
        DataFromOR = OR.readlines()
        LengthOf_DataFromOR = len(DataFromOR)

        for iterationVariable_One in range(0, LengthOf_DataFromOR):
            LengthOf_Element = len(DataFromOR[iterationVariable_One])
            COUNTER_MAJOR = 0

            if LengthOf_Element >= 3:
                for iterationVariable_Two in KeysOfSuffixDictionary:

                    if COUNTER_MAJOR == 1:
                        break
                    else:
                        SuffixDictionaryValue_ForKey = SuffixDictionary[iterationVariable_Two]
                        COUNTER_MINOR = 0

                        TotalSpaceMovement_ForKey = SuffixDictionaryValue_ForKey[0]
                        for iterationVariable_Three in range(2, TotalSpaceMovement_ForKey + 2):
                            if DataFromOR[iterationVariable_One][LengthOf_Element - iterationVariable_Three] == \
                                    SuffixDictionaryValue_ForKey[iterationVariable_Three - 1]:
                                COUNTER_MINOR = COUNTER_MINOR + 1

                        if COUNTER_MINOR == SuffixDictionaryValue_ForKey[0]:
                            DataFromOR[iterationVariable_One] = ''.join(
                                DataFromOR[iterationVariable_One][subIterationVariable] for subIterationVariable in
                                range(0, LengthOf_Element - (TotalSpaceMovement_ForKey + 1)))
                            if SuffixDictionaryValue_ForKey[TotalSpaceMovement_ForKey + 1] != '':
                                DataFromOR[iterationVariable_One] = DataFromOR[iterationVariable_One] + \
                                                                    SuffixDictionaryValue_ForKey[
                                                                        TotalSpaceMovement_ForKey + 1]
                            DataFromOR[iterationVariable_One] = DataFromOR[iterationVariable_One] + '\n'
                            COUNTER_MAJOR = COUNTER_MAJOR + 1

    OR.close()

    with open(FileName, 'w', encoding='utf-8') as OW:
        for iterationVariable_Four in DataFromOR:
            OW.write(iterationVariable_Four)
    OW.close()


stemming()

duplicatesRemoval()
