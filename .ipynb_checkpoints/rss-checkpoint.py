
# import socket
# from ast import literal_eval
# import random

# HOST = '0.0.0.0'
# PORT = 5002

# WIDTH = 800
# HEIGHT = 600
# SEG_SIZE = 20

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     s.bind((HOST, PORT))
#     s.listen()
#     print(f"Server listening on {HOST}:{PORT}")

#     while True:
#         client_sock, client_addr = s.accept()
#         print('New connection from', client_addr)

#         while True:
#             data = client_sock.recv(1024)
#             if data:
#                 print(f"Received: {data.decode()}")
#                 yx1, yy1, yx2, yy2, x1, y1, x2, y2, ax, ay = literal_eval(data.decode())

#                 print(x1, y1, x2, y2, "yellow:", yx1, yy1, yx2, yy2, "apple:", ax, ay)

#                 # Chase apple while ensuring no out-of-bounds movement
#                 move_options = []

#                 if x1 < ax and x1 + SEG_SIZE < WIDTH:  # Move right if safe
#                     move_options.append("Right")
#                 elif x1 > ax and x1 - SEG_SIZE >= 0:  # Move left if safe
#                     move_options.append("Left")

#                 if y1 < ay and y1 + SEG_SIZE < HEIGHT:  # Move down if safe
#                     move_options.append("Down")
#                 elif y1 > ay and y1 - SEG_SIZE >= 0:  # Move up if safe
#                     move_options.append("Up")

#                 if move_options:
#                     data_to_proxy = random.choice(move_options)
#                 else:
#                     # Random safe movement if no valid move towards apple
#                     safe_moves = []
#                     if x1 + SEG_SIZE < WIDTH:
#                         safe_moves.append("Right")
#                     if x1 - SEG_SIZE >= 0:
#                         safe_moves.append("Left")
#                     if y1 + SEG_SIZE < HEIGHT:
#                         safe_moves.append("Down")
#                     if y1 - SEG_SIZE >= 0:
#                         safe_moves.append("Up")

#                     data_to_proxy = random.choice(safe_moves) if safe_moves else "Straight"

#                 print(f"Sending direction: {data_to_proxy}")
#                 client_sock.sendall(data_to_proxy.encode())

#             else:
#                 break

#         client_sock.close()
#     s.close()
#-----------------------------------------------------------------------------------------------------------------------------------------------------------


# import socket
# from ast import literal_eval
# import random

# # Constants
# HOST = '0.0.0.0'
# PORT = 5002

# WIDTH = 800
# HEIGHT = 600
# SEG_SIZE = 20

# def validate_data(data):
#     """Validate if the received data is in the correct format."""
#     try:
#         yx1, yy1, yx2, yy2, x1, y1, x2, y2, ax, ay = literal_eval(data.decode())
#         return yx1, yy1, yx2, yy2, x1, y1, x2, y2, ax, ay
#     except Exception as e:
#         print(f"Error parsing data: {e}")
#         return None

# def get_safe_moves(x, y):
#     """Get a list of safe moves for the current position."""
#     safe_moves = []
#     if x + SEG_SIZE < WIDTH:
#         safe_moves.append("Right")
#     if x - SEG_SIZE >= 0:
#         safe_moves.append("Left")
#     if y + SEG_SIZE < HEIGHT:
#         safe_moves.append("Down")
#     if y - SEG_SIZE >= 0:
#         safe_moves.append("Up")
#     return safe_moves

# def get_move_towards_apple(x, y, ax, ay):
#     """Determine the best move towards the apple."""
#     move_options = []

#     if x < ax and x + SEG_SIZE < WIDTH:  # Move right if safe
#         move_options.append("Right")
#     elif x > ax and x - SEG_SIZE >= 0:  # Move left if safe
#         move_options.append("Left")

#     if y < ay and y + SEG_SIZE < HEIGHT:  # Move down if safe
#         move_options.append("Down")
#     elif y > ay and y - SEG_SIZE >= 0:  # Move up if safe
#         move_options.append("Up")

#     return move_options

# def avoid_collision(yx1, yy1, yx2, yy2, x, y):
#     """Check if a move would result in a collision with the yellow snake."""
#     potential_collisions = [(yx1, yy1), (yx2, yy2)]
    
#     def would_collide(move):
#         new_x, new_y = x, y
#         if move == "Right":
#             new_x += SEG_SIZE
#         elif move == "Left":
#             new_x -= SEG_SIZE
#         elif move == "Down":
#             new_y += SEG_SIZE
#         elif move == "Up":
#             new_y -= SEG_SIZE
        
#         return (new_x, new_y) in potential_collisions
    
#     return would_collide

# def main():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen()
#         print(f"Server listening on {HOST}:{PORT}")

#         while True:
#             client_sock, client_addr = s.accept()
#             print('New connection from', client_addr)

#             while True:
#                 try:
#                     data = client_sock.recv(1024)
#                     if data:
#                         print(f"Received: {data.decode()}")
#                         parsed_data = validate_data(data)
#                         if parsed_data:
#                             yx1, yy1, yx2, yy2, x1, y1, x2, y2, ax, ay = parsed_data
#                             print(x1, y1, x2, y2, "yellow:", yx1, yy1, yx2, yy2, "apple:", ax, ay)

#                             # Determine safe moves towards the apple
#                             move_options = get_move_towards_apple(x1, y1, ax, ay)
#                             collision_check = avoid_collision(yx1, yy1, yx2, yy2, x1, y1)

#                             safe_moves_towards_apple = [move for move in move_options if not collision_check(move)]

#                             if safe_moves_towards_apple:
#                                 data_to_proxy = random.choice(safe_moves_towards_apple)
#                             else:
#                                 # If no safe moves towards apple, choose a random safe move
#                                 safe_moves = get_safe_moves(x1, y1)
#                                 safe_moves_without_collision = [move for move in safe_moves if not collision_check(move)]
#                                 data_to_proxy = random.choice(safe_moves_without_collision) if safe_moves_without_collision else "Straight"

#                             print(f"Sending direction: {data_to_proxy}")
#                             client_sock.sendall(data_to_proxy.encode())

#                         else:
#                             print("Invalid data received.")
#                     else:
#                         break

#                 except Exception as e:
#                     print(f"An error occurred: {e}")
#                     break

#             client_sock.close()
#         s.close()

# if __name__ == "__main__":
#     main()


# .........................................................................................
# import socket
# from ast import literal_eval
# import random
# import keepalive

# HOST = '0.0.0.0'
# PORT = 5002

# WIDTH = 800
# HEIGHT = 600
# SEG_SIZE = 20

# def determine_move(x1, y1, ax, ay):
#     move_options = []

#     if x1 < ax and x1 + SEG_SIZE < WIDTH:  
#         move_options.append("Right")
#     elif x1 > ax and x1 - SEG_SIZE >= 0:  
#         move_options.append("Left")

#     if y1 < ay and y1 + SEG_SIZE < HEIGHT:  
#         move_options.append("Down")
#     elif y1 > ay and y1 - SEG_SIZE >= 0:  
#         move_options.append("Up")

#     if move_options:
#         return random.choice(move_options)
#     else:
#         safe_moves = []
#         if x1 + SEG_SIZE < WIDTH:
#             safe_moves.append("Right")
#         if x1 - SEG_SIZE >= 0:
#             safe_moves.append("Left")
#         if y1 + SEG_SIZE < HEIGHT:
#             safe_moves.append("Down")
#         if y1 - SEG_SIZE >= 0:
#             safe_moves.append("Up")

#         return random.choice(safe_moves) if safe_moves else "Straight"
# def determine_aggressive_move(x1, y1, yx1, yy1, ax, ay):
#     move_options = []
#     potential_moves = [(yx1 + SEG_SIZE, yy1), (yx1 - SEG_SIZE, yy1), (yx1, yy1 + SEG_SIZE), (yx1, yy1 - SEG_SIZE)]

#     # Prioritize moving toward the opponent's head
#     if (x1 + SEG_SIZE, y1) in potential_moves and x1 + SEG_SIZE < WIDTH:
#         move_options.append("Right")
#     if (x1 - SEG_SIZE, y1) in potential_moves and x1 - SEG_SIZE >= 0:
#         move_options.append("Left")
#     if (x1, y1 + SEG_SIZE) in potential_moves and y1 + SEG_SIZE < HEIGHT:
#         move_options.append("Down")
#     if (x1, y1 - SEG_SIZE) in potential_moves and y1 - SEG_SIZE >= 0:
#         move_options.append("Up")

#     # If no aggressive moves are possible, chase the apple
#     if not move_options:
#         if x1 < ax and x1 + SEG_SIZE < WIDTH:
#             move_options.append("Right")
#         elif x1 > ax and x1 - SEG_SIZE >= 0:
#             move_options.append("Left")
#         if y1 < ay and y1 + SEG_SIZE < HEIGHT:
#             move_options.append("Down")
#         elif y1 > ay and y1 - SEG_SIZE >= 0:
#             move_options.append("Up")

#     return random.choice(move_options) if move_options else "Straight"

# def movement_generator():
#     while True:
#         # Determine the next move based on your strategy
#         # For now, just yield a random move
#         yield random.choice(["Right", "Left", "Up", "Down"])

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     keepalive.set(s)  # Enable keepalive
#     s.bind((HOST, PORT))
#     s.listen()
#     print(f"Server listening on {HOST}:{PORT}")

#     while True:
#         client_sock, client_addr = s.accept()
#         keepalive.set(client_sock)  # Enable keepalive on client socket
#         print('New connection from', client_addr)

#         move_gen = movement_generator()  # Initialize the movement generator

#         while True:
#             data = client_sock.recv(1024)
#             if data:
#                 print(f"Received: {data.decode()}")
#                 yx1, yy1, yx2, yy2, x1, y1, x2, y2, ax, ay = literal_eval(data.decode())

#                 print(x1, y1, x2, y2, "yellow:", yx1, yy1, yx2, yy2, "apple:", ax, ay)

#                 # Use the movement generator to get the next move
#                 # For now, just use the determine_move function
#                 move = determine_move(x1, y1, ax, ay)
#                 # Alternatively, use next(move_gen) to get a move from the generator
#                 print(f"Sending direction: {move}")
#                 client_sock.sendall(move.encode())

#             else:
#                 break

#         client_sock.close()
# .......................................................................................................................................

# 
# def determine_rss_move(rx1, ry1, x1, y1, ax, ay, rx2, ry2, x2, y2):
#     # Calculate snake lengths using head-tail positions
#     rss_len = calculate_snake_length(rx1, ry1, rx2, ry2)
#     yss_len = calculate_snake_length(x1, y1, x2, y2)
    
#     move_options = []
#     defensive_mode = rss_len <= yss_len or abs(rx1 - x1) + abs(ry1 - y1) < 3 * SEG_SIZE

#     # Helper function to check if a move is safe
#     def is_safe_move(new_x, new_y):
#         # Check boundaries
#         if not (0 <= new_x < WIDTH and 0 <= new_y < HEIGHT):
#             return False
#         # Check collision with opponent head
#         if new_x == x1 and new_y == y1:
#             return False
#         # Check collision with own tail (approximate)
#         if abs(new_x - rx2) + abs(new_y - ry2) < rss_len * SEG_SIZE * 0.5:
#             return False
#         return True

#     # Priority 1: Move toward apple if safe and not in defensive mode
#     if not defensive_mode:
#         if rx1 < ax and is_safe_move(rx1 + SEG_SIZE, ry1):
#             move_options.append("Right")
#         if rx1 > ax and is_safe_move(rx1 - SEG_SIZE, ry1):
#             move_options.append("Left")
#         if ry1 < ay and is_safe_move(rx1, ry1 + SEG_SIZE):
#             move_options.append("Down")
#         if ry1 > ay and is_safe_move(rx1, ry1 - SEG_SIZE):
#             move_options.append("Up")

#     # Priority 2: Defensive moves if too close to opponent or in defensive mode
#     if defensive_mode or not move_options:
#         dx = rx1 - x1
#         dy = ry1 - y1
#         move_options = []  # Reset options for defensive priority
        
#         # Move away from opponent head
#         if dx > 0 and is_safe_move(rx1 - SEG_SIZE, ry1):
#             move_options.append("Left")
#         elif dx < 0 and is_safe_move(rx1 + SEG_SIZE, ry1):
#             move_options.append("Right")
#         if dy > 0 and is_safe_move(rx1, ry1 - SEG_SIZE):
#             move_options.append("Up")
#         elif dy < 0 and is_safe_move(rx1, ry1 + SEG_SIZE):
#             move_options.append("Down")

#     # Priority 3: Fallback - explore safe moves if no preferred options
#     if not move_options:
#         for direction, (dx, dy) in [("Right", (SEG_SIZE, 0)), ("Left", (-SEG_SIZE, 0)),
#                                  ("Down", (0, SEG_SIZE)), ("Up", (0, -SEG_SIZE))]:
#             new_x, new_y = rx1 + dx, ry1 + dy
#             if is_safe_move(new_x, new_y):
#                 move_options.append(direction)

#     # Priority 4: If near boundary, prioritize moves away from walls
#     if not move_options or (rx1 < SEG_SIZE or rx1 > WIDTH - 2*SEG_SIZE or 
#                           ry1 < SEG_SIZE or ry1 > HEIGHT - 2*SEG_SIZE):
#         safe_boundary_moves = []
#         if rx1 < SEG_SIZE and is_safe_move(rx1 + SEG_SIZE, ry1):
#             safe_boundary_moves.append("Right")
#         if rx1 > WIDTH - 2*SEG_SIZE and is_safe_move(rx1 - SEG_SIZE, ry1):
#             safe_boundary_moves.append("Left")
#         if ry1 < SEG_SIZE and is_safe_move(rx1, ry1 + SEG_SIZE):
#             safe_boundary_moves.append("Down")
#         if ry1 > HEIGHT - 2*SEG_SIZE and is_safe_move(rx1, ry1 - SEG_SIZE):
#             safe_boundary_moves.append("Up")
#         if safe_boundary_moves:
#             move_options = safe_boundary_moves

#     # Final fallback: Random safe move or "Straight" if trapped
#     return random.choice(move_options) if move_options else "Straight"


# import socket
# from ast import literal_eval
# import random

# HOST = '0.0.0.0'  
# PORT = 5002  # Port for red snake

# WIDTH = 800
# HEIGHT = 600
# SEG_SIZE = 20

# def determine_rss_move(rx1, ry1, x1, y1, ax, ay):
#     move_options = []
    
#     # Defensive strategy to avoid YSS while still heading to apple
#     if rx1 < ax and rx1 + SEG_SIZE < WIDTH and not (rx1 + SEG_SIZE == x1 and ry1 == y1):
#         move_options.append("Right")
#     elif rx1 > ax and rx1 - SEG_SIZE >= 0 and not (rx1 - SEG_SIZE == x1 and ry1 == y1):
#         move_options.append("Left")

#     if ry1 < ay and ry1 + SEG_SIZE < HEIGHT and not (ry1 + SEG_SIZE == y1 and rx1 == x1):
#         move_options.append("Down")
#     elif ry1 > ay and ry1 - SEG_SIZE >= 0 and not (ry1 - SEG_SIZE == y1 and rx1 == x1):
#         move_options.append("Up")
    
#     return random.choice(move_options) if move_options else "Straight"

# def handle_rss():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen()
#         print(f"Red Snake Server listening on {HOST}:{PORT}")

#         while True:
#             client_sock, client_addr = s.accept()
#             print('New connection from', client_addr)

#             while True:
#                 data = client_sock.recv(1024)
#                 if data:
#                     x1, y1, x2, y2, rx1, ry1, rx2, ry2, ax, ay = literal_eval(data.decode())
#                     move = determine_rss_move(rx1, ry1, x1, y1, ax, ay)
#                     client_sock.sendall(move.encode())
#                 else:
#                     break

#             client_sock.close()

# # Run both servers separately
# import threading
# threading.Thread(target=handle_rss).start()

import socket
from ast import literal_eval
import random
from collections import deque

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 5002      # Port for red snake
WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20

# Store recent positions to detect patterns
last_positions = deque(maxlen=10)
last_opponent_positions = deque(maxlen=10)

def manhattan_distance(x1, y1, x2, y2):
    """Calculate Manhattan distance between two points"""
    return abs(x1 - x2) + abs(y1 - y2)

def is_collision_danger(rx1, ry1, yx1, yy1, direction):
    """Check if moving in a direction puts us at risk of collision"""
    new_x, new_y = rx1, ry1
    
    if direction == "Right":
        new_x += SEG_SIZE
    elif direction == "Left":
        new_x -= SEG_SIZE
    elif direction == "Down":
        new_y += SEG_SIZE
    elif direction == "Up":
        new_y -= SEG_SIZE
    
    # Check for immediate collision with opponent head
    if new_x == yx1 and new_y == yy1:
        return True
    
    # Also check one step ahead for potential traps
    opponent_direction = predict_opponent_direction(yx1, yy1)
    if opponent_direction:
        next_yx, next_yy = yx1, yy1
        if opponent_direction == "Right":
            next_yx += SEG_SIZE
        elif opponent_direction == "Left":
            next_yx -= SEG_SIZE
        elif opponent_direction == "Down":
            next_yy += SEG_SIZE
        elif opponent_direction == "Up":
            next_yy -= SEG_SIZE
            
        # Check if we'd be in the opponent's next position
        if new_x == next_yx and new_y == next_yy:
            return True
    
    return False

def predict_opponent_direction(yx1, yy1):
    """Try to predict opponent's next move based on recent positions"""
    if len(last_opponent_positions) < 2:
        return None
    
    # Get last two positions
    prev_yx, prev_yy = last_opponent_positions[-2]
    
    # Calculate movement vector
    dx = yx1 - prev_yx
    dy = yy1 - prev_yy
    
    if dx > 0:
        return "Right"
    elif dx < 0:
        return "Left"
    elif dy > 0:
        return "Down"
    elif dy < 0:
        return "Up"
    
    return None

def get_safe_moves(rx1, ry1, yx1, yy1):
    """Get all valid moves that don't hit walls or cause immediate collisions"""
    possible_moves = []
    
    # Check all four directions
    if rx1 + SEG_SIZE < WIDTH - SEG_SIZE:
        possible_moves.append("Right")
    if rx1 - SEG_SIZE > SEG_SIZE:
        possible_moves.append("Left")
    if ry1 + SEG_SIZE < HEIGHT - SEG_SIZE:
        possible_moves.append("Down")
    if ry1 - SEG_SIZE > SEG_SIZE:
        possible_moves.append("Up")
    
    # Filter out dangerous moves
    safe_moves = [m for m in possible_moves if not is_collision_danger(rx1, ry1, yx1, yy1, m)]
    
    return safe_moves or possible_moves  # If no safe moves, return all possible moves

def can_trap_opponent(rx1, ry1, yx1, yy1):
    """Check if we can execute a trapping maneuver on the opponent"""
    # Calculate what direction the opponent is moving
    opponent_direction = predict_opponent_direction(yx1, yy1)
    if not opponent_direction:
        return None
    
    # Check if we're in position to intercept opponent's path
    dist = manhattan_distance(rx1, ry1, yx1, yy1)
    
    # Only attempt trapping if we're in the sweet spot - close enough to trap
    # but not too close to be dangerous
    if dist < 2 * SEG_SIZE or dist > 4 * SEG_SIZE:
        return None
    
    # Determine where the opponent will be in the next move
    next_yx, next_yy = yx1, yy1
    if opponent_direction == "Right":
        next_yx += SEG_SIZE
    elif opponent_direction == "Left":
        next_yx -= SEG_SIZE
    elif opponent_direction == "Down":
        next_yy += SEG_SIZE
    elif opponent_direction == "Up":
        next_yy -= SEG_SIZE
    
    # Check if we can move to intercept the opponent's path safely
    possible_trap_moves = []
    
    # Check wall proximity for safety
    is_near_wall = (
        yx1 <= 2 * SEG_SIZE or 
        yx1 >= WIDTH - 2 * SEG_SIZE or 
        yy1 <= 2 * SEG_SIZE or 
        yy1 >= HEIGHT - 2 * SEG_SIZE
    )
    
    # Don't attempt traps near walls (too risky)
    if is_near_wall:
        return None
    
    # Only try perpendicular interception (safer and more effective)
    if opponent_direction in ["Right", "Left"]:
        # If opponent is moving horizontally, check if we can move vertically to intercept
        if abs(rx1 - next_yx) <= SEG_SIZE and abs(ry1 - next_yy) == SEG_SIZE:
            if ry1 < next_yy and ry1 + SEG_SIZE < HEIGHT - 2 * SEG_SIZE:
                possible_trap_moves.append("Down")
            elif ry1 > next_yy and ry1 - SEG_SIZE > 2 * SEG_SIZE:
                possible_trap_moves.append("Up")
    elif opponent_direction in ["Up", "Down"]:
        # If opponent is moving vertically, check if we can move horizontally to intercept
        if abs(ry1 - next_yy) <= SEG_SIZE and abs(rx1 - next_yx) == SEG_SIZE:
            if rx1 < next_yx and rx1 + SEG_SIZE < WIDTH - 2 * SEG_SIZE:
                possible_trap_moves.append("Right")
            elif rx1 > next_yx and rx1 - SEG_SIZE > 2 * SEG_SIZE:
                possible_trap_moves.append("Left")
    
    # If we have possible trap moves, choose one (prefer the safest)
    if possible_trap_moves:
        return possible_trap_moves[0]  # Just take the first one for consistency
    
    return None

def calculate_move_scores(rx1, ry1, yx1, yy1, ax, ay, moves):
    """Score moves based on multiple factors"""
    scores = []
    
    # Calculate apple distance
    apple_dist = manhattan_distance(rx1, ry1, ax, ay)
    
    # Check if we can execute a trapping maneuver
    trap_move = can_trap_opponent(rx1, ry1, yx1, yy1)
    
    # Score all possible moves
    for move in moves:
        new_x, new_y = rx1, ry1
        
        if move == "Right":
            new_x += SEG_SIZE
        elif move == "Left":
            new_x -= SEG_SIZE
        elif move == "Down":
            new_y += SEG_SIZE
        elif move == "Up":
            new_y -= SEG_SIZE
        
        # Calculate base score from apple distance
        new_apple_dist = manhattan_distance(new_x, new_y, ax, ay)
        score = 1000 - new_apple_dist  # Convert to a score where higher is better
        
        # Add bonus for moves that increase distance from opponent
        current_dist_to_opponent = manhattan_distance(rx1, ry1, yx1, yy1)
        new_dist_to_opponent = manhattan_distance(new_x, new_y, yx1, yy1)
        
        # If we're close to opponent, reward moves that increase distance
        if current_dist_to_opponent < 5 * SEG_SIZE and new_dist_to_opponent > current_dist_to_opponent:
            score += 50
        
        # Avoid getting trapped against walls
        wall_proximity = 0
        if new_x <= 2 * SEG_SIZE or new_x >= WIDTH - 2 * SEG_SIZE:
            wall_proximity += 1
        if new_y <= 2 * SEG_SIZE or new_y >= HEIGHT - 2 * SEG_SIZE:
            wall_proximity += 1
            
        # Penalize moves that put us close to walls on two sides (corner situations)
        if wall_proximity >= 2:
            score -= 100
            
        # Apply trap bonus only if:
        # 1. It's a valid trap move
        # 2. We're not too close to an apple (prioritize eating)
        # 3. We're not too close to a wall (avoid risky traps)
        if move == trap_move and apple_dist > 3 * SEG_SIZE and wall_proximity == 0:
            # Give trap bonus but don't make it overwhelmingly high
            # This will make trapping favorable but not override apple pursuit in most cases
            score += 200
            
        scores.append((move, score))
    
    # Sort by score (descending)
    scores.sort(key=lambda x: x[1], reverse=True)
    return scores

def handle_client():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        print(f"Red Snake Server listening on {HOST}:{PORT}")
        
        while True:
            client_sock, client_addr = s.accept()
            print('New connection from', client_addr)
            
            # Reset tracking for new game
            last_positions.clear()
            last_opponent_positions.clear()
            
            while True:
                data = client_sock.recv(1024)
                if data:
                    try:
                        # Parse game state
                        yx1, yy1, yx2, yy2, rx1, ry1, rx2, ry2, ax, ay = literal_eval(data.decode())
                        
                        # Track positions
                        last_positions.append((rx1, ry1))
                        last_opponent_positions.append((yx1, yy1))
                        
                        # Wall avoidance (absolute priority)
                        if max(rx1, rx2) >= WIDTH - SEG_SIZE:
                            move = "Left"
                        elif min(rx1, rx2) <= SEG_SIZE:
                            move = "Right"
                        elif max(ry1, ry2) >= HEIGHT - SEG_SIZE:
                            move = "Up"
                        elif min(ry1, ry2) <= SEG_SIZE:
                            move = "Down"
                        else:
                            # Get all safe moves
                            safe_moves = get_safe_moves(rx1, ry1, yx1, yy1)
                            
                            if not safe_moves:
                                # No safe moves, just try to avoid walls
                                if rx1 + SEG_SIZE < WIDTH - SEG_SIZE:
                                    move = "Right"
                                elif rx1 - SEG_SIZE > SEG_SIZE:
                                    move = "Left"
                                elif ry1 + SEG_SIZE < HEIGHT - SEG_SIZE:
                                    move = "Down"
                                else:
                                    move = "Up"
                            else:
                                # Calculate scores for each move
                                scored_moves = calculate_move_scores(rx1, ry1, yx1, yy1, ax, ay, safe_moves)
                                
                                # Choose best move
                                move = scored_moves[0][0]
                                
                                # Add a small random element to be unpredictable (5% chance)
                                if random.random() < 0.05 and len(scored_moves) > 1:
                                    move = random.choice(safe_moves)
                        
                        client_sock.sendall(move.encode())
                        
                    except Exception as e:
                        print(f"Error processing data: {e}")
                        client_sock.sendall("Straight".encode())
                else:
                    break
                    
            client_sock.close()

if __name__ == "__main__":
    handle_client()