from django.shortcuts import render
import cohere
import re
from cohere.responses.classify import Example

# Create your views here.
def classify(request):
    if request.method == 'POST':
        input_text = request.POST['input_text']
        co = cohere.Client('BwCfMf2xNrEOxHz26N56JuTvmihY36v8eYe0EEfn')
        response = co.classify(
            model='large',
            inputs=[input_text],
            examples=[Example("My order was cancelled but I was not refunded yet.", "Technical support"), Example("I am having trouble resetting my password", "Technical support"), Example(" Can you tell me more about your return policy?", "Technical support"), Example("I just purchased your device, but my computer doesn\'t seem to recognize it. Can you please provide me with some troubleshooting steps?\n\n\n", "Technical support"), Example("I\'m having trouble connecting to your server. Can you please help me troubleshoot this issue?\n\n\n", "Technical support"), Example("I\'m trying to understand the charges on my recent invoice. Can you please provide me with a breakdown of the charges?\n\n\n", "Billing inquiry"), Example(" I would like to change my payment plan. Can you please help me with this?\n\n\n", "Billing inquiry"), Example("I just received a late payment notice for my subscription. Can you please explain why this happened and what I can do to avoid it in the future?\n\n\n", "Billing inquiry"), Example("I received a defective product. Can you please help me with a replacement or refund?\n\n\n", "Billing inquiry"), Example("How often do you rebalance your investment portfolios?", "Billing inquiry"), Example("What is the monthly fee on the investment accounts?", "Billing inquiry"), Example("How can I withdraw funds from my investment account?", "Billing inquiry"), Example("I\'m having trouble installing your product on my computer. Can you please guide me through the installation process?\n\n\n", "Billing inquiry"), Example("How can I minimize my tax exposure?", "Product issue"), Example("I forgot my account password and I\'m unable to log in. Can you please help me reset my password?\n\n\n", "Product issue"), Example("I would like to terminate my account. Can you please guide me through the account termination process?\n\n\n", "Product issue"), Example("I\'m having trouble creating an account on your website. Can you please guide me through the account creation process?\n\n\n", "Product issue"), Example("When will I get my tax refund back?", "Product issue"), Example("How much does it cost to use your tax filing platform?", "Product issue"), Example("I\'d like to increase my monthly RRSP contributions to my RRSP", "Account management"), Example("I want to take advantage of the First Time Home Buyers program and take money out of my RRSP.  How does the program work?", "Account management"), Example("What is the ${currentYear} RRSP limit?", "Account management"), Example("Does your system ensure I won\'t overcontribute to my RRSP?", "Account management"), Example("How do I set up employer contributions to my RRSP", "Account management"), Example("My subscription was cancelled but I still have access to the service.", "Account management")])


        classification_str = str(response.classifications[0])
        classification_str = re.sub(r'Classification<', '', classification_str)
        classification_str = re.sub(r'>', '', classification_str)
        res = classification_str.split(",")
        for t in res:
            temp = t.split(":")
            if temp[0] == "prediction":
                prediction = temp[1]


        return render(request, 'results.html', {'prediction': prediction})

    else:
        return render(request, 'classify.html')
