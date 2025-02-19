import gymnasium as gym

NOP = 0
LEFT_ENGINE = 1
MAIN_ENGINE = 2
RIGHT_ENGINE = 3


def get_agent_action(percepts):
    x, y, x_speed, y_speed, angle = percepts[:5]

    # Fire main engine to keep from crashing
    if y_speed < -0.1 and -0.5 < angle < 0.5:
        return MAIN_ENGINE

    # Generally try to stay level
    if angle < -0.2:
        return LEFT_ENGINE
    if angle > 0.2:
        return RIGHT_ENGINE

    # Rotate to fire main engine in opposite direction
    # if we are moving laterally
    if x_speed < -0.1:
        return RIGHT_ENGINE
    if x_speed > 0.1:
        return LEFT_ENGINE

    return NOP


def run_graphical():
    with gym.make("LunarLander-v3", render_mode="human") as env:
        total_reward = 0.0
        percepts, info = env.reset()
        while True:
            action = get_agent_action(percepts)
            percepts, reward, terminated, truncated, info = env.step(action)
            done = terminated or truncated
            total_reward += reward

            if env.render() == False:
                break

            if done:
                print(f"Total reward: {total_reward}")
                break


def get_average_reward(num_runs=20):
    with gym.make("LunarLander-v3") as env:
        print(f"Calculating average performance over {num_runs} runs")
        avg_reward = 0.0
        for i in range(num_runs):
            percepts, info = env.reset()
            total_reward = 0.0
            while True:
                action = get_agent_action(percepts)
                percepts, reward, terminated, truncated, info = env.step(action)
                done = terminated or truncated
                total_reward += reward

                if done:
                    print(f"Simulation {i} reward: {total_reward}")
                    avg_reward += total_reward / num_runs
                    break

    return avg_reward


if __name__ == "__main__":
    run_graphical()

    print(f"Average reward over 20 runs: {get_average_reward(20)}")
