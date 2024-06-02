# recommender.py

from surprise import KNNWithMeans

# The options for using user_based, cosine similarities #
sim_options = {
    "name": "cosine",
    "user_based": False,  # To find similarities between items #
}
algo = KNNWithMeans(sim_options=sim_options)