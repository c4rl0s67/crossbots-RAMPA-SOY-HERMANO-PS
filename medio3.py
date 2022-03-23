import random
 
state   = 'straight'
counter = 0

def control(inputs):
    global state
    global counter

    front_left  = inputs["front-left"]
    front_right = inputs["front-right"]
    distance_left = inputs["distance-left"] 
    distance_right = inputs["distance-right"]
    
    if distance_left == 0 or distance_right == 0 :
        state = 'turning'
        counter  = random.randint(10, 20)
    if state == 'straight':

        if front_left != 0 or front_right != 0 :
            state    = 'turning'
            counter  = random.randint(10, 20)
        else:
            state    = 'straight'
        
        
            
    elif state == 'turning':
        
        if counter > 0:
            counter -= 1
            state    = 'turning'
        else:    
            state    = 'straight'

    speed = 20;

    
    left_speed  = speed
    right_speed = speed
   
        
    if state == 'straight':

        left_speed  =  speed
        right_speed = -speed
            
    elif state == 'turning':

        left_speed  =  speed
        right_speed =  speed
        
    
 
        

    return {
        'leftSpeed':  left_speed,
        'rightSpeed': right_speed,
        'log': [
            { 'name': 'Left',  'value':   left_speed,    'min': -45, 'max': 45 },
            { 'name': 'Right', 'value':   right_speed,   'min': -45, 'max': 45 }
        ]
    }