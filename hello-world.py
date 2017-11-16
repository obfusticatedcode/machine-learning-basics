from sklearn import tree
# replacing "smooth" with 1 and "bumpy" with 0
# replacing "orange" with 1 and "apple" with 0
features = [[140, 1], [130, 1], [150, 0], [170, 0]]
labels = [0, 0, 1, 1]
clf = tree.DecisionTreeClassifier()
clf = clf.fit(features, labels)
print(clf.predict([[160, 0]]))
