import numpy as np
import airsim

def indoor_meta():

    orig_ip = [     #x, y, theta in DEGREES

                    # One - Pyramid
                    [-21593, -1563, -45],  # Player Start
                    [-22059, -2617, -45],
                    [-22800, -3489, 90],

                    # Two - FrogEyes
                    [-15744, -1679, 0],
                    [-15539, -3043, 180],
                    [-13792, -3371, 90],

                    # Three - UpDown
                    [-11221, -3171, 180],
                    [-9962, -3193, 0],
                    [-7464, -4558, 90],

                    # Four - Long
                    [-649, -4287, 180],  # Player Start
                    [-4224, -2601, 180],
                    [1180, -2153, -90],

                    # Five - VanLeer
                    [6400, -4731, 90],  # Player Start
                    [5992, -2736, 180],
                    [8143, -2835, -90],

                    # Six - Complex_Indoor
                    [11320, -2948, 0],
                    [12546, -3415, -180],
                    [10809, -2106, 0],

                    # Seven - Techno
                    [19081, -8867, 0],
                    [17348, -3864, -120],
                    [20895, -4757, 30],

                    # Eight - GT
                    [26042, -4336, 180],
                    [26668, -3070, 0],
                    [27873, -2792, -135]



                ]# x, y, theta
    level_name = [
                    'Pyramid1', 'Pyramid2', 'Pyramid3',
                    'FrogEyes1', 'FrogEyes2', 'FrogEyes3',
                    'UpDown1', 'UpDown2', 'UpDown3',
                    'Long1', 'Long2', 'Long3',
                    'VanLeer1', 'VanLeer2', 'VanLeer3',
                    'ComplexIndoor1', 'ComplexIndoor2', 'ComplexIndoor3',
                    'Techno1', 'Techno2', 'Techno3',
                    'GT1', 'GT2', 'GT3',
                ]
    crash_threshold = 0.07
    initZ = -1
    return orig_ip, level_name, crash_threshold, initZ

# Test condo indoor initial positions

def indoor_condo():
    orig_ip =   [
                  [-290, -1700, 0], # Player start
                   [580, 1200, 180],
                   [-240, -500, 90]
                ]
    level_name = ['Condo1', 'Condo2', 'Condo3']
    crash_threshold = 0.07
    initZ = -2
    return orig_ip, level_name, crash_threshold, initZ

def indoor_techno():
    orig_ip = [
        [19081, -8867, 0],
        [17348, -3864, -120],
        [20895, -4757, 30]
    ]
    level_name = ['Techno1', 'Techno2', 'Techno3']
    crash_threshold = 0.07
    initZ = -2
    return orig_ip, level_name, crash_threshold, initZ

def indoor_long():
    orig_ip = [
        [-649, -4287, 180],  # Player Start
        [-4224, -2601, 180],
        [1180, -2153, -90],
        [2058, -3184, 50],
        [1644,-1464, 15],
        [-3754, -4302, 0]
    ]
    level_name = ['Long1', 'Long2', 'Long3', 'Long4', 'Long5', 'Long6']
    crash_threshold = 0.07
    initZ = -1
    return orig_ip, level_name, crash_threshold, initZ

# Four - Long

# Seven - Techno





def indoor_twisty():
    orig_ip =   [
                  [127, -770, 90], # Player start
                   [2209, -115, 180],
                   [1680, 1590, -145]
                ]
    level_name = ['Twisty1', 'Twisty2', 'Twisty3']
    crash_threshold = 0.07
    initZ = -2
    return orig_ip, level_name, crash_threshold, initZ

def indoor_pretzel():
    orig_ip =   [
                  [3308, 650, 180], # Player start
                   [3330, -200, -160],
                   [1480, -1040, 25]
                ]
    level_name = ['Cloud1', 'Cloud2', 'Cloud3']
    crash_threshold = 0.07
    initZ = -1.5
    return orig_ip, level_name, crash_threshold, initZ

def initial_positions(name):
    name = name+'()'
    orig_ip, level_name, crash_threshold, initZ = eval(name)
    player_start_unreal=orig_ip[0]
    reset_array = []

    for i in range(0, len(orig_ip)):
        x1 = (orig_ip[i][0]-player_start_unreal[0])/100
        y1 = (orig_ip[i][1]-player_start_unreal[1])/100
        z1 = initZ
        pitch = 0
        roll = 0
        yaw = orig_ip[i][2]*np.pi/180
        pp = airsim.Pose(airsim.Vector3r(x1, y1, z1), airsim.to_quaternion(pitch, roll, yaw))
        reset_array.append(pp)

    return reset_array, level_name, crash_threshold, initZ
