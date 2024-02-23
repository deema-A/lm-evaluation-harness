import datasets

def process_docs(dataset: datasets.Dataset):
    def _helper(doc):
      # modifies the contents of a single
      # document in our dataset.
      doc["choices"] = [doc["choices"][0], doc["choices"][1], doc["choices"][2]]
      doc["gold"] = doc["choices"][doc["answer_index"]]
      return doc

    return dataset.map(_helper) # returns back a datasets.Dataset object