from transformers import pipeline


# def summary_bart(text, len):

#     summarizer = pipeline("summarization")
#     summary_text = summarizer(text, max_length=len, min_length=150, do_sample=False)[0][
#         "summary_text"
#     ]
#     return summary_text


def summary_t5_small(text, len):

    summarizer = pipeline(
        "summarization",
        model="t5-small",
        tokenizer="t5-small",
        framework="pt",
    )
    summary_text = summarizer(text, max_length=len, min_length=150, do_sample=False)[0][
        "summary_text"
    ]
    return summary_text


if __name__ == "__main__":
    data = """In this form, I think it is clear that this indeed is an epistemological argument. It is not a claim about metaphysics per se, it is a claim about what we can ultimately know regardless of the subject.
    Now, many people object that this would state that human knowledge was (as a matter of fact) defective in some way, in the sense that we lack the cognitive abilities to fully understand ultimate Reality. Kant was a famous proponent of this view. But that is not the claim here.
    Basically, the claim is rather about what Heidegger and Gadamer called the hermeneutic circle and Plessner, more broadly, the anthropological circle: Every reflection on existence is, by necessity, a reflection of human beings through human minds. This means that even though we have very good reasons to assume that our understanding of the world is broadly accurate and one way to map ultimate Reality (whatever that may be, given it exists), it still may well be that there are other layers and aspects which simply elude our (current?) abilities and way of understanding things. Think of it like the relation between a map and the actual terrain: no matter how good the map is, making claims about the map is very different from making claims about the terrain itself. Knowing this, absolute positive claims about metaphysics are necessarily dubious.
    This is not to say that absolute metaphysical claims are wrong, nor that there are other forms of knowledge - that is why it is not self-refuting. It just says that a) strictly speaking, what we say about metaphysics is about how the world is to us, it is about "our" world, ie. we simply cannot know what it is like independent from our understanding, ie. in an absolute, objective way, and b) even if this kind of nitpicking is completely irrelevant for most of human lives and practices, it matters to keep that in mind when doing metaphysics. Doubting that the car rushing at you is real and pondering ways in which coexistence of different corporal objects in the same space would be possible does not exactly prolong your life, yet when you do philosophical metaphysics, dealing with sceptical objections is your bread and butter.
    Long story short: It is an epistemological claim which bids not to pretend we had some divine ability to transcend human existence when it comes to metaphysics. This includes the possibility that this kind of (human) thought itself is unnecessarily cautious and everyday metaphysical claims are indeed spot-on, we simply cannot know: Who's to judge if not some form of intelligent being which has a 'higher' point of view from outside existence as we know it? And even if that existed (obviously in a way different from how we and the world do), it would obviously transcend our existence and thus wouldn't be able to tell us since otherwise, it would share existence with us which would in turn prevent it from having said higher standpoint....well...at least as far as we are able to think about these kinds of things  """
    data2 = """ Close to a million doses — over 951,000, to be more exact — made their way into the arms of Americans in the past 24 hours, the U.S. Centers for Disease Control and Prevention reported Wednesday. That’s the largest number of shots given in one day since the rollout began and a big jump from the previous day, when just under 340,000 doses were given, CBS News reported.
    That number is likely to jump quickly after the federal government on Tuesday gave states the OK to vaccinate anyone over 65 and said it would release all the doses of vaccine it has available for distribution. Meanwhile, a number of states have now opened mass vaccination sites in an effort to get larger numbers of people inoculated, CBS News reported. """
    print(summary_t5_small(data, 500))
    print(summary_t5_small(data2, 150))
