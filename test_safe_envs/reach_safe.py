import gym
import panda_gym
import time
# env = gym.make("PandaReach-v2", render=True)
env = gym.make("PandaReachSafe-v2", render=True)
obs_dim = env.observation_space.shape
# print(obs_dim)

obs = env.reset()
# print(obs.shape)
done = False

while not done:
    action = env.action_space.sample()
    obs, cost_reward, done, info = env.step(action)
    # print(obs.shape)
    env.render(mode='human')
    # time.sleep(9)


env.close()
