from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk

nltk.download("stopwords")
nltk.download("punkt")

stopWords = set(stopwords.words("english"))


def getSummary(text, length):
    # print("Text recived => ", text)
    # cleaning sub
    clean_sub = ""
    for p in text.split("\n"):
        if p:
            clean_sub += p + "."

    # Tokenizing the text
    words = word_tokenize(text)

    # creating Frequency table
    freqTable = dict()

    for word in words:
        word = word.lower()
        if word in stopWords:
            continue
        if word in freqTable:
            freqTable[word] += 1
        else:
            freqTable[word] = 1

    maximum_frequncy = max(freqTable.values())

    for word in freqTable.keys():
        freqTable[word] = freqTable[word] / maximum_frequncy

    # print("words freq =>", freqTable)

    # print("Word tokenizing and frequency table created")

    sentences = sent_tokenize(clean_sub)
    # print(sentences)
    sentenceValues = dict()
    # print("sentences =>", sentences)

    for sentence in sentences:
        for word, freq in freqTable.items():
            if word in sentence.lower():
                if sentence in sentenceValues:
                    sentenceValues[sentence] += freq
                else:
                    sentenceValues[sentence] = freq
    # print("sentencesValue =>", sentenceValues)

    # print("Sentence creation and sentence Value table created")

    sumValues = 0
    for sentence in sentenceValues:
        sumValues += sentenceValues[sentence]

    # print("sumValues =>", sumValues)

    average = sumValues / len(sentenceValues)
    # print("average => ", average)
    summary = ""
    # print("Summary creation")
    # print('Subtitle => ', text)

    # print(f'In sentence formation for summary : ')

    for sentence in sentences:
        # print(f"{sentence} {sentenceValues[sentence]} > {1.2 * average}")
        if (sentence in sentenceValues) and (
            sentenceValues[sentence] > (1.2 * average)
        ):
            summary += " " + sentence

    # print('summary => ', summary)

    return summary


def summary_test():
    text = """
    Something started everything. That something is the prime mover, or unmoved mover, as Aristotle called it. That something may be external or it may be the universe itself; in which case, the universe is its own starter. The universe being its own cause may seem impossible, but when dealing with subjects like these, at the edge of and beyond our existence (and therefore comprehension), ineffable possibilities must be considered. If time is circular, then the last moment of the universe starts the first moment of the universe, and in such an event, the universe creates itself.
    So, that's the first dichotomous question. Was the universe started by something outside of the universe, or did the universe start itself? Is an external force the prime mover, or is the universe itself the prime mover? Then comes the second dichotomous question: is the prime mover conscious or not? Now, exactly what consciousness is, is a scientific, semantic and philosophical mess. So, for the purposes of simplicity and universality, I've defined conscious as any level of experience (and thus awareness). If the prime mover experiences existence, it is to some degree aware of existence, and is therefore by my definition of consciousness, conscious.
    So, the prime mover may be conscious, or it may not. If the former, there is a creator, if the latter, there is not. Again, for simplicity, I'm defining the creator as the conscious prime mover. The prime mover may not have consciously created the universe, but if they are conscious, and they created it, then they are the creator. Here's a diagram.
    My original thought was then that this means there's a 50% chance of there being a creator and a 50% that there isn't one. This is based on the fact that the creator is not necessarily bound by our universe. They are not necessarily materialistic. As such, for both of those reasons, we may not have access to any information regarding the probability of whether there's a creator or not. There may not exist any possible proof (if going by our current understanding and knowledge, there are no proofs that could prove a creator, though the possibility of a currently ineffable proof provided by the creator themselves must be considered). Science deals strictly with the falsifiable and material, so there's no help there either. Essentially, we have no objective information supporting one side or the other. Because of that, the probability of what the correct answer is is dictated by the number of options. There are two options, as such, the probability of either being correct is 50%.
    """
    text2 = """
    You've been stranded thousands
    of miles from homewith no money or possessions.Such a predicament would make many
    people despair and curse their awful fate.But for Zeno of Cyprus, it became the
    foundation of his life's work and legacy.The once wealthy merchant lost everything
    when he was shipwrecked in Athensaround 300 BCE.With not much else to do,
    he wandered into a book shop,became intrigued by reading about Socrates,and proceeded to seek out and study
    with the city's noted philosophers.As Zeno began educating his own students,he originated the philosophy
    known as Stoicism,whose teachings of virtue, tolerance,
    and self-controlhave inspired generations of thinkers
    and leaders.The name Stoicism comes 
    from the Stoa Poikile,the decorated public colonnadewhere Zeno and his disciples gathered
    for discussion.Today, we colloquially 
    use the word stoicto mean someone who 
    remains calm under pressureand avoids emotional extremes.But while this captures important
    aspects of Stoicism,the original philosophy was more
    than just an attitude.The Stoics believed that 
    everything around usoperates according 
    to a web of cause and effect,resulting in a rational structure
    of the universe,which they called logos.And while we may not always
    have control over the events affecting us,we can have control over 
    how we approach things.Rather than imagining an ideal society,the Stoic tries to deal 
    with the world as it iswhile pursuing self-improvement
    through four cardinal virtues:practical wisdom,the ability to navigate complex situations
    in a logical, informed, and calm manner;temperance,the exercise of self-restraint 
    and moderation in all aspects of life;justice,treating others with fairness even
    when they have done wrong;and courage,not just in extraordinary circumstances,but facing daily challenges
    with clarity and integrity.As Seneca, one of the most famous
    Roman Stoics wrote,"Sometimes, even to live 
    is an act of courage."But while Stoicism focuses on 
    personal improvement,it's not a self-centered philosophy.At a time when Roman laws considered
    slaves as property,Seneca called for their humane treatmentand stressed that we all share
    the same fundamental humanity.Nor does Stoicism encourage passivity.The idea is that only people 
    who have cultivatedvirtue and self-control in themselves
    can bring positive change in others.One of the most famous Stoic writers
    was also one of Rome's greatest emperors.Over the course of his 19-year reign,Stoicism gave Marcus Aurelius the resolve
    to lead the Empire through two major wars,while dealing with the loss of many
    of his children.Centuries later, Marcus's journals would
    guide and comfort Nelson Mandelathrough his 27-year imprisonmentduring his struggle 
    for racial equality in South Africa.After his release and eventual victory,
    Mandela stressed peace and reconciliation,believing that while the injustices
    of the past couldn't be changed,his people could confront them
    in the presentand seek to build a better,
    more just future.Stoicism was an active school 
    of philosophy for several centuriesin Greece and Rome.As a formal institution, it faded away,but its influence has continued
    to this day.Christian theologians, 
    such as Thomas Aquinas,have admired and adopted its focus
    on the virtues,and there are parallels between
    Stoic Ataraxia, or tranquility of mind,and the Buddhist concept of Nirvana.One particularly influential Stoic
    was the philosopher Epictetuswho wrote that suffering stemsnot from the events in our lives,
    but from our judgements about them.This has resonated strongly
    with modern psychologyand the self-help movement.For example, rational emotive
    behavioral therapyfocuses on changing 
    the self-defeating attitudespeople form about 
    their life circumstances.There's also Viktor Frankl's logotherapy.Informed by Frankl's own time
    as a concentration camp prisoner,logotherapy is based on 
    the Stoic principlethat we can harness our will power
    to fill our lives with meaning,even in the bleakest situations.
    """

    print(getSummary(text2, 150))


if __name__ == "__main__":
    summary_test()
