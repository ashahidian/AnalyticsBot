cd sempre && ./run @mode=simple -Grammar.inPaths analyticsBot/interface.grammar \
    -FeatureExtractor.featureDomains rule -Dataset.inPaths train:analyticsBot/interface.examples \
    -Learner.maxTrainIters 3

