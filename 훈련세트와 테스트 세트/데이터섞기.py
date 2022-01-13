# import numpy as np
# import matplotlib.pyplot as plt

# fish data가 있다고 가정

# input_arr=np.array(fish_data) 0~35로 가정
# target_arr=np.array(fish_target) 35번째부터로 가정
# np.random.seed(42)
# index=np.arange(49)
# np.radom.shuffle(index)



# train_input= input_arr[index[:35]]
# train_target=target_arr[index[:35]]
# test_input= input_arr[index[35:]]
# test_target= target_arr[index[35:]]

# plt.scatter(train_input[:,0],train_input[:,1])
# plt.scatter(test_input[:,0], test_input[:,1])
# plt.xlabel('length')
# plt.ylabel('weight')
# plt.show()

# kn=kn.fit(train_input, train_target)
# kn.score(test_input, test_target)


