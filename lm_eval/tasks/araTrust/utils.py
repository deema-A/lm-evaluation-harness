import datasets

def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
      # modifies the contents of a single
      # document in our dataset.
    #   doc["choices"] = [doc["choice1"], doc["choice2"], doc["wrong_answer"]]
    #   doc["gold"] = doc["label"]
    #   return doc

    # return dataset.map(_helper) # returns back a datasets.Dataset object

      doc["choices"] = [i.split(')')[1] for i in doc['Choices'].split('\n')]
      doc["choice0"] = doc['Choices'].split('\n')[0].replace(')','.')
      doc["choice1"] = doc['Choices'].split('\n')[1].replace(')','.')
      doc["choice2"] = doc['Choices'].split('\n')[2].replace(')','.')
      doc["choice3"] = doc['Choices'].split('\n')[3].replace(')','.')

      char2num = { 'أ': 0,
            'ب': 1,
            'ج': 2,
            'د': 3,
        }

      doc["gold"] = char2num[doc["Gold"]]
    #   print(doc["gold"])
      return doc

    return dataset.map(_helper) # returns back a datasets.Dataset object