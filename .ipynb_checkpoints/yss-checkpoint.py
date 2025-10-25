
# import socket
# from ast import literal_eval
# import random

# HOST = '0.0.0.0'
# PORT = 5001  # Port for the yellow snake

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
#                 x1, y1, x2, y2, rx1, ry1, rx2, ry2, ax, ay = literal_eval(data.decode())

#                 print(x1, y1, x2, y2, "red:", rx1, ry1, rx2, ry2, "apple:", ax, ay)

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
# #---------------------------------------------------------------------------------------------------------------------------------------------------

# import socket
# from ast import literal_eval
# import random

# HOST = '0.0.0.0'
# PORT = 5001  

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

# def set_keepalive(sock):
#     sock.setsockopt(socket.SOL_SOCKET, socket.SO_KEEPALIVE, 1)
#     # Optional: Set keepalive parameters (Linux-specific)
#     # sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPIDLE, 60)  # 1 minute idle
#     # sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPINTVL, 10)  # 10 seconds interval
#     # sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_KEEPCNT, 5)  # 5 probes

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     set_keepalive(s)  # Enable keepalive
#     s.bind((HOST, PORT))
#     s.listen()
#     print(f"Server listening on {HOST}:{PORT}")

#     while True:
#         client_sock, client_addr = s.accept()
#         set_keepalive(client_sock)  # Enable keepalive on client socket
#         client_sock.settimeout(180)  # 3 minutes timeout for inactivity
#         print('New connection from', client_addr)

#         while True:
#             try:
#                 data = client_sock.recv(1024)
#                 if data:
#                     print(f"Received: {data.decode()}")
#                     x1, y1, x2, y2, rx1, ry1, rx2, ry2, ax, ay = literal_eval(data.decode())

#                     print(x1, y1, x2, y2, "red:", rx1, ry1, rx2, ry2, "apple:", ax, ay)

#                     move = determine_move(x1, y1, ax, ay)
#                     print(f"Sending direction: {move}")
#                     client_sock.sendall(move.encode())
#                 else:
#                     break
#             except socket.timeout:
#                 print("Connection timed out due to inactivity.")
#                 break

#         client_sock.close()
#................................................................................................................
# import socket
# from ast import literal_eval
# import random
# import keepalive

# HOST = '0.0.0.0'
# PORT = 5001  

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
#                 x1, y1, x2, y2, rx1, ry1, rx2, ry2, ax, ay = literal_eval(data.decode())

#                 print(x1, y1, x2, y2, "red:", rx1, ry1, rx2, ry2, "apple:", ax, ay)

#                 # Use the movement generator to get the next move
#                 # For now, just use the determine_move function
#                 move = determine_move(x1, y1, ax, ay)
#                 # Alternatively, use next(move_gen) to get a move from the generator
#                 print(f"Sending direction: {move}")
#                 client_sock.sendall(move.encode())

#             else:
#                 break

#         client_sock.close()
#...................................................................................



# import socket
# from ast import literal_eval
# import random

# HOST = '0.0.0.0'  # Listen on all available interfaces
# PORT = 5001      # Port for yellow snake
# WIDTH = 800
# HEIGHT = 600
# SEG_SIZE = 20

# def manhattan_distance(x1, y1, x2, y2):
#     """Calculate Manhattan distance between two points"""
#     return abs(x1 - x2) + abs(y1 - y2)

# def will_collide(yx1, yy1, rx1, ry1, move_dir):
#     """Check if moving in the given direction will cause a collision with the red snake"""
#     new_x, new_y = yx1, yy1
    
#     if move_dir == "Right":
#         new_x += SEG_SIZE
#     elif move_dir == "Left":
#         new_x -= SEG_SIZE
#     elif move_dir == "Down":
#         new_y += SEG_SIZE
#     elif move_dir == "Up":
#         new_y -= SEG_SIZE
        
#     # Check if the new position collides with the red snake's head
#     return new_x == rx1 and new_y == ry1

# def determine_move(yx1, yy1, rx1, ry1, ax, ay):
#     """
#     Aggressive strategy with improved collision detection:
#     - Go directly for apple when possible
#     - Detect and avoid collisions with red snake
#     """
#     # Determine direct moves to apple - aggressive approach
#     move_options = []
    
#     # Prioritize moves that get us closer to the apple (aggressive)
#     if yx1 < ax and yx1 + SEG_SIZE < WIDTH:
#         move_options.append("Right")
#     elif yx1 > ax and yx1 - SEG_SIZE >= 0:
#         move_options.append("Left")
#     if yy1 < ay and yy1 + SEG_SIZE < HEIGHT:
#         move_options.append("Down")
#     elif yy1 > ay and yy1 - SEG_SIZE >= 0:
#         move_options.append("Up")
    
#     # If we have no good move options, generate all possible moves
#     if not move_options:
#         if yx1 + SEG_SIZE < WIDTH:
#             move_options.append("Right")
#         if yx1 - SEG_SIZE >= 0:
#             move_options.append("Left")
#         if yy1 + SEG_SIZE < HEIGHT:
#             move_options.append("Down")
#         if yy1 - SEG_SIZE >= 0:
#             move_options.append("Up")
    
#     # If still no options, go straight
#     if not move_options:
#         return "Straight"
    
#     # Filter out moves that would cause collision with red snake
#     safe_moves = [move for move in move_options if not will_collide(yx1, yy1, rx1, ry1, move)]
    
#     # If there are safe moves, choose the one that gets us closest to the apple
#     if safe_moves:
#         move_scores = []
#         for move_dir in safe_moves:
#             new_x, new_y = yx1, yy1
            
#             if move_dir == "Right":
#                 new_x += SEG_SIZE
#             elif move_dir == "Left":
#                 new_x -= SEG_SIZE
#             elif move_dir == "Down":
#                 new_y += SEG_SIZE
#             elif move_dir == "Up":
#                 new_y -= SEG_SIZE
                
#             # Calculate distance to apple
#             apple_dist = manhattan_distance(new_x, new_y, ax, ay)
#             move_scores.append((move_dir, apple_dist))
        
#         # Sort by distance to apple (ascending)
#         move_scores.sort(key=lambda x: x[1])
#         return move_scores[0][0]
    
#     # If all moves are unsafe, choose the one that takes us away from red snake
#     else:
#         # In emergency situations, choose a move that maximizes distance from red snake
#         evasive_moves = []
#         for move_dir in move_options:
#             new_x, new_y = yx1, yy1
            
#             if move_dir == "Right":
#                 new_x += SEG_SIZE
#             elif move_dir == "Left":
#                 new_x -= SEG_SIZE
#             elif move_dir == "Down":
#                 new_y += SEG_SIZE
#             elif move_dir == "Up":
#                 new_y -= SEG_SIZE
                
#             # Calculate distance to red snake
#             snake_dist = manhattan_distance(new_x, new_y, rx1, ry1)
#             evasive_moves.append((move_dir, snake_dist))
        
#         # Sort by distance to red snake (descending)
#         evasive_moves.sort(key=lambda x: x[1], reverse=True)
#         return evasive_moves[0][0]

# def handle_client():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen()
#         print(f"Yellow Snake Server listening on {HOST}:{PORT}")
        
#         while True:
#             # Accept new connections
#             client_sock, client_addr = s.accept()
#             print('New connection from', client_addr)

#             while True:
#                 data = client_sock.recv(1024)
#                 if data:
#                     try:
#                         # Parse game state
#                         yx1, yy1, yx2, yy2, rx1, ry1, rx2, ry2, ax, ay = literal_eval(data.decode())
                        
#                         # First priority: avoid walls
#                         if max(yx1, yx2) >= WIDTH - SEG_SIZE:
#                             move = "Left"
#                         elif min(yx1, yx2) <= SEG_SIZE:
#                             move = "Right"
#                         elif max(yy1, yy2) >= HEIGHT - SEG_SIZE:
#                             move = "Up"
#                         elif min(yy1, yy2) <= SEG_SIZE:
#                             move = "Down"
#                         else:
#                             # Determine best move 
#                             move = determine_move(yx1, yy1, rx1, ry1, ax, ay)
                        
#                         client_sock.sendall(move.encode())
                        
#                     except Exception as e:
#                         print(f"Error processing data: {e}")
#                         client_sock.sendall("Straight".encode())
#                 else:
#                     break
                    
#             client_sock.close()

# if __name__ == "__main__":
#     handle_client()


#..........................
# import socket
# from ast import literal_eval
# import random

# HOST = '0.0.0.0'  # Listen on all available interfaces
# PORT = 5001      # Port for yellow snake
# WIDTH = 800
# HEIGHT = 600
# SEG_SIZE = 20

# def manhattan_distance(x1, y1, x2, y2):
#     """Calculate Manhattan distance between two points"""
#     return abs(x1 - x2) + abs(y1 - y2)

# def is_collision_imminent(yx1, yy1, rx1, ry1, direction):
#     """Check if following the given direction would cause an immediate collision with red snake"""
#     new_x, new_y = yx1, yy1
    
#     if direction == "Right":
#         new_x += SEG_SIZE
#     elif direction == "Left":
#         new_x -= SEG_SIZE
#     elif direction == "Down":
#         new_y += SEG_SIZE
#     elif direction == "Up":
#         new_y -= SEG_SIZE
    
#     return new_x == rx1 and new_y == ry1

# def determine_direct_path(yx1, yy1, ax, ay):
#     """Determine the most direct path to the apple"""
#     # Calculate horizontal and vertical distances to apple
#     x_dist = ax - yx1
#     y_dist = ay - yy1
    
#     # Horizontal movement priority (matching red snake behavior)
#     if abs(x_dist) > 0:
#         return "Right" if x_dist > 0 else "Left"
#     elif abs(y_dist) > 0:
#         return "Down" if y_dist > 0 else "Up"
    
#     return None  # No direct path needed (at apple)

# def get_all_valid_moves(yx1, yy1):
#     """Get all valid moves that won't hit walls"""
#     valid_moves = []
    
#     if yx1 + SEG_SIZE < WIDTH - SEG_SIZE:
#         valid_moves.append("Right")
#     if yx1 - SEG_SIZE > SEG_SIZE:
#         valid_moves.append("Left")
#     if yy1 + SEG_SIZE < HEIGHT - SEG_SIZE:
#         valid_moves.append("Down")
#     if yy1 - SEG_SIZE > SEG_SIZE:
#         valid_moves.append("Up")
        
#     return valid_moves

# def handle_client():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen()
#         print(f"Yellow Snake Server listening on {HOST}:{PORT}")
        
#         while True:
#             client_sock, client_addr = s.accept()
#             print('New connection from', client_addr)
            
#             while True:
#                 data = client_sock.recv(1024)
#                 if data:
#                     try:
#                         # Parse game state
#                         yx1, yy1, yx2, yy2, rx1, ry1, rx2, ry2, ax, ay = literal_eval(data.decode())
                        
#                         # First priority: avoid walls (mandatory)
#                         if max(yx1, yx2) >= WIDTH - SEG_SIZE:
#                             move = "Left"
#                         elif min(yx1, yx2) <= SEG_SIZE:
#                             move = "Right"
#                         elif max(yy1, yy2) >= HEIGHT - SEG_SIZE:
#                             move = "Up"
#                         elif min(yy1, yy2) <= SEG_SIZE:
#                             move = "Down"
#                         else:
#                             # Determine direct path to apple
#                             direct_move = determine_direct_path(yx1, yy1, ax, ay)
                            
#                             # Check if direct move would cause collision
#                             if direct_move and is_collision_imminent(yx1, yy1, rx1, ry1, direct_move):
#                                 # Collision detected - find alternative
#                                 valid_moves = get_all_valid_moves(yx1, yy1)
                                
#                                 # Remove any moves that would cause collision
#                                 safe_moves = [m for m in valid_moves if not is_collision_imminent(yx1, yy1, rx1, ry1, m)]
                                
#                                 if safe_moves:
#                                     # Find the next best move (that gets us closest to apple)
#                                     move_scores = []
#                                     for m in safe_moves:
#                                         new_x, new_y = yx1, yy1
                                        
#                                         if m == "Right":
#                                             new_x += SEG_SIZE
#                                         elif m == "Left":
#                                             new_x -= SEG_SIZE
#                                         elif m == "Down":
#                                             new_y += SEG_SIZE
#                                         elif m == "Up":
#                                             new_y -= SEG_SIZE
                                            
#                                         dist = manhattan_distance(new_x, new_y, ax, ay)
#                                         move_scores.append((m, dist))
                                    
#                                     # Sort by distance (ascending)
#                                     move_scores.sort(key=lambda x: x[1])
                                    
#                                     # Take the best alternative move
#                                     move = move_scores[0][0]
#                                 else:
#                                     # No safe moves - move away from red snake
#                                     move = "Up" if direct_move != "Up" else "Down"  # Default escape
#                             else:
#                                 # No collision - proceed with direct path
#                                 move = direct_move
                        
#                         client_sock.sendall(move.encode())
                        
#                     except Exception as e:
#                         print(f"Error processing data: {e}")
#                         client_sock.sendall("Straight".encode())
#                 else:
#                     break
                    
#             client_sock.close()

# if __name__ == "__main__":
#     handle_client()

# import socket
# from ast import literal_eval
# import random

# HOST = '0.0.0.0'  # Listen on all available interfaces
# PORT = 5001      # Port for yellow snake
# WIDTH = 800
# HEIGHT = 600
# SEG_SIZE = 20

# def manhattan_distance(x1, y1, x2, y2):
#     """Calculate Manhattan distance between two points"""
#     return abs(x1 - x2) + abs(y1 - y2)

# def predict_red_snake_movement(rx1, ry1, ax, ay):
#     """Predict where the red snake is likely to move based on apple position"""
#     # The red snake typically moves directly toward the apple
#     x_dist = ax - rx1
#     y_dist = ay - ry1
    
#     if abs(x_dist) > abs(y_dist):
#         return (rx1 + (SEG_SIZE if x_dist > 0 else -SEG_SIZE), ry1)
#     else:
#         return (rx1, ry1 + (SEG_SIZE if y_dist > 0 else -SEG_SIZE))

# def is_perpendicular_trap(yx1, yy1, rx1, ry1, direction):
#     """
#     Detect if the red snake is setting up a perpendicular trap
#     This happens when red snake is moving perpendicular to our path
#     """
#     # Current direction of yellow snake
#     dx, dy = 0, 0
#     if direction == "Right":
#         dx = 1
#     elif direction == "Left":
#         dx = -1
#     elif direction == "Down":
#         dy = 1
#     elif direction == "Up":
#         dy = -1
        
#     # Check if red snake is near our path and perpendicular to it
#     if abs(yx1 - rx1) <= SEG_SIZE * 2 and abs(yy1 - ry1) <= SEG_SIZE * 2:
#         # If we're moving horizontally and red snake is above or below
#         if dx != 0 and abs(yy1 - ry1) <= SEG_SIZE:
#             return True
#         # If we're moving vertically and red snake is to the left or right
#         if dy != 0 and abs(yx1 - rx1) <= SEG_SIZE:
#             return True
    
#     return False

# def is_collision_imminent(yx1, yy1, rx1, ry1, direction):
#     """Check if following the given direction would cause an immediate collision with red snake"""
#     new_x, new_y = yx1, yy1
    
#     if direction == "Right":
#         new_x += SEG_SIZE
#     elif direction == "Left":
#         new_x -= SEG_SIZE
#     elif direction == "Down":
#         new_y += SEG_SIZE
#     elif direction == "Up":
#         new_y -= SEG_SIZE
    
#     return new_x == rx1 and new_y == ry1

# def determine_direct_path(yx1, yy1, ax, ay):
#     """Determine the most direct path to the apple"""
#     # Calculate horizontal and vertical distances to apple
#     x_dist = ax - yx1
#     y_dist = ay - yy1
    
#     # For equal distances, choose vertical movement first (opposite of red snake's strategy)
#     if abs(x_dist) == abs(y_dist):
#         return "Down" if y_dist > 0 else "Up"
    
#     # Otherwise prioritize the longest distance to cover
#     if abs(x_dist) > abs(y_dist):
#         return "Right" if x_dist > 0 else "Left"
#     else:
#         return "Down" if y_dist > 0 else "Up"
    
#     return None  # No direct path needed (at apple)

# def get_all_valid_moves(yx1, yy1):
#     """Get all valid moves that won't hit walls"""
#     valid_moves = []
    
#     if yx1 + SEG_SIZE < WIDTH - SEG_SIZE:
#         valid_moves.append("Right")
#     if yx1 - SEG_SIZE > SEG_SIZE:
#         valid_moves.append("Left")
#     if yy1 + SEG_SIZE < HEIGHT - SEG_SIZE:
#         valid_moves.append("Down")
#     if yy1 - SEG_SIZE > SEG_SIZE:
#         valid_moves.append("Up")
        
#     return valid_moves

# def handle_client():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen()
#         print(f"Yellow Snake Server listening on {HOST}:{PORT}")
        
#         # Track previous red snake position to detect movement patterns
#         prev_rx, prev_ry = None, None
        
#         while True:
#             client_sock, client_addr = s.accept()
#             print('New connection from', client_addr)
            
#             while True:
#                 data = client_sock.recv(1024)
#                 if data:
#                     try:
#                         # Parse game state
#                         yx1, yy1, yx2, yy2, rx1, ry1, rx2, ry2, ax, ay = literal_eval(data.decode())
                        
#                         # Track red snake movement
#                         if prev_rx is not None and prev_ry is not None:
#                             red_dx = rx1 - prev_rx
#                             red_dy = ry1 - prev_ry
                            
#                         prev_rx, prev_ry = rx1, ry1
                        
#                         # First priority: avoid walls (mandatory)
#                         if max(yx1, yx2) >= WIDTH - SEG_SIZE:
#                             move = "Left"
#                         elif min(yx1, yx2) <= SEG_SIZE:
#                             move = "Right"
#                         elif max(yy1, yy2) >= HEIGHT - SEG_SIZE:
#                             move = "Up"
#                         elif min(yy1, yy2) <= SEG_SIZE:
#                             move = "Down"
#                         else:
#                             # Determine direct path to apple
#                             direct_move = determine_direct_path(yx1, yy1, ax, ay)
                            
#                             # Calculate distances
#                             distance_to_apple = manhattan_distance(yx1, yy1, ax, ay)
#                             distance_to_red = manhattan_distance(yx1, yy1, rx1, ry1)
                            
#                             # Check if red snake is nearby and setting a trap
#                             if distance_to_red < SEG_SIZE * 3 and is_perpendicular_trap(yx1, yy1, rx1, ry1, direct_move):
#                                 # Perpendicular trap detected - change strategy
#                                 valid_moves = get_all_valid_moves(yx1, yy1)
                                
#                                 # Find moves that aren't in the direction of the red snake
#                                 safe_moves = []
#                                 for m in valid_moves:
#                                     new_x, new_y = yx1, yy1
#                                     if m == "Right":
#                                         new_x += SEG_SIZE
#                                     elif m == "Left":
#                                         new_x -= SEG_SIZE
#                                     elif m == "Down":
#                                         new_y += SEG_SIZE
#                                     elif m == "Up":
#                                         new_y -= SEG_SIZE
                                    
#                                     # Avoid moving directly toward red snake
#                                     if manhattan_distance(new_x, new_y, rx1, ry1) >= distance_to_red:
#                                         safe_moves.append(m)
                                
#                                 if safe_moves:
#                                     # Choose the move that gets us closer to the apple
#                                     move_scores = []
#                                     for m in safe_moves:
#                                         new_x, new_y = yx1, yy1
#                                         if m == "Right":
#                                             new_x += SEG_SIZE
#                                         elif m == "Left":
#                                             new_x -= SEG_SIZE
#                                         elif m == "Down":
#                                             new_y += SEG_SIZE
#                                         elif m == "Up":
#                                             new_y -= SEG_SIZE
                                            
#                                         dist = manhattan_distance(new_x, new_y, ax, ay)
#                                         move_scores.append((m, dist))
                                    
#                                     # Sort by distance (ascending)
#                                     move_scores.sort(key=lambda x: x[1])
#                                     move = move_scores[0][0]
#                                 else:
#                                     # No safe moves - take an emergency turn
#                                     move = "Up" if direct_move != "Up" and direct_move != "Down" else "Right"
                            
#                             # Check if direct move would cause collision
#                             elif direct_move and is_collision_imminent(yx1, yy1, rx1, ry1, direct_move):
#                                 # Collision detected - find alternative
#                                 valid_moves = get_all_valid_moves(yx1, yy1)
                                
#                                 # Remove any moves that would cause collision
#                                 safe_moves = [m for m in valid_moves if not is_collision_imminent(yx1, yy1, rx1, ry1, m)]
                                
#                                 if safe_moves:
#                                     # Find the next best move (that gets us closest to apple)
#                                     move_scores = []
#                                     for m in safe_moves:
#                                         new_x, new_y = yx1, yy1
#                                         if m == "Right":
#                                             new_x += SEG_SIZE
#                                         elif m == "Left":
#                                             new_x -= SEG_SIZE
#                                         elif m == "Down":
#                                             new_y += SEG_SIZE
#                                         elif m == "Up":
#                                             new_y -= SEG_SIZE
                                            
#                                         dist = manhattan_distance(new_x, new_y, ax, ay)
#                                         move_scores.append((m, dist))
                                    
#                                     # Sort by distance (ascending)
#                                     move_scores.sort(key=lambda x: x[1])
#                                     move = move_scores[0][0]
#                                 else:
#                                     # No safe moves - move away from red snake
#                                     move = "Up" if direct_move != "Up" else "Down"  # Default escape
#                             else:
#                                 # No collision danger - proceed with direct path
#                                 move = direct_move
                        
#                         client_sock.sendall(move.encode())
                        
#                     except Exception as e:
#                         print(f"Error processing data: {e}")
#                         client_sock.sendall("Straight".encode())
#                 else:
#                     break
                    
#             client_sock.close()
#             # Reset tracking when game ends
#             prev_rx, prev_ry = None, None

# if __name__ == "__main__":
#     handle_client()
# import socket
# from ast import literal_eval
# import random

# HOST = '0.0.0.0'  # Listen on all available interfaces
# PORT = 5001      # Port for yellow snake
# WIDTH = 800
# HEIGHT = 600
# SEG_SIZE = 20

# def manhattan_distance(x1, y1, x2, y2):
#     """Calculate Manhattan distance between two points"""
#     return abs(x1 - x2) + abs(y1 - y2)

# def will_collide(yx1, yy1, rx1, ry1, direction):
#     """Check if moving in the given direction will cause a collision"""
#     new_x, new_y = yx1, yy1
    
#     if direction == "Right":
#         new_x += SEG_SIZE
#     elif direction == "Left":
#         new_x -= SEG_SIZE
#     elif direction == "Down":
#         new_y += SEG_SIZE
#     elif direction == "Up":
#         new_y -= SEG_SIZE
    
#     # Check if new position would collide with red snake's head
#     return new_x == rx1 and new_y == ry1

# def get_valid_moves(yx1, yy1):
#     """Get all valid moves that don't hit walls"""
#     valid_moves = []
    
#     if yx1 + SEG_SIZE < WIDTH - SEG_SIZE:
#         valid_moves.append("Right")
#     if yx1 - SEG_SIZE > SEG_SIZE:
#         valid_moves.append("Left")
#     if yy1 + SEG_SIZE < HEIGHT - SEG_SIZE:
#         valid_moves.append("Down")
#     if yy1 - SEG_SIZE > SEG_SIZE:
#         valid_moves.append("Up")
        
#     return valid_moves

# def handle_client():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen()
#         print(f"Yellow Snake Server listening on {HOST}:{PORT}")
        
#         while True:
#             client_sock, client_addr = s.accept()
#             print('New connection from', client_addr)
            
#             while True:
#                 data = client_sock.recv(1024)
#                 if data:
#                     try:
#                         # Parse game state
#                         yx1, yy1, yx2, yy2, rx1, ry1, rx2, ry2, ax, ay = literal_eval(data.decode())
                        
#                         # Handle wall avoidance first (no choice here)
#                         if max(yx1, yx2) >= WIDTH - SEG_SIZE:
#                             move = "Left"
#                         elif min(yx1, yx2) <= SEG_SIZE:
#                             move = "Right"
#                         elif max(yy1, yy2) >= HEIGHT - SEG_SIZE:
#                             move = "Up"
#                         elif min(yy1, yy2) <= SEG_SIZE:
#                             move = "Down"
#                         else:
#                             # Get all valid moves
#                             valid_moves = get_valid_moves(yx1, yy1)
                            
#                             # Remove moves that would collide with red snake
#                             safe_moves = [m for m in valid_moves if not will_collide(yx1, yy1, rx1, ry1, m)]
                            
#                             # If no safe moves, panic and take any valid move
#                             if not safe_moves:
#                                 move = valid_moves[0] if valid_moves else "Straight"
#                             else:
#                                 # Calculate distances to apple for each safe move
#                                 move_scores = []
                                
#                                 for m in safe_moves:
#                                     new_x, new_y = yx1, yy1
                                    
#                                     if m == "Right":
#                                         new_x += SEG_SIZE
#                                     elif m == "Left":
#                                         new_x -= SEG_SIZE
#                                     elif m == "Down":
#                                         new_y += SEG_SIZE
#                                     elif m == "Up":
#                                         new_y -= SEG_SIZE
                                    
#                                     # Calculate distance to apple
#                                     dist_to_apple = manhattan_distance(new_x, new_y, ax, ay)
#                                     move_scores.append((m, dist_to_apple))
                                
#                                 # Sort by distance to apple (ascending)
#                                 move_scores.sort(key=lambda x: x[1])
                                
#                                 # Choose the move that gets closest to apple
#                                 move = move_scores[0][0]
                        
#                         client_sock.sendall(move.encode())
                        
#                     except Exception as e:
#                         print(f"Error processing data: {e}")
#                         client_sock.sendall("Straight".encode())
#                 else:
#                     break
                    
#             client_sock.close()

# if __name__ == "__main__":
#     handle_client()

# import socket
# from ast import literal_eval
# import random

# HOST = '0.0.0.0'  # Listen on all available interfaces
# PORT = 5001      # Port for yellow snake
# WIDTH = 800
# HEIGHT = 600
# SEG_SIZE = 20

# def handle_client():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen()
#         print(f"Yellow Snake Server listening on {HOST}:{PORT}")
        
#         # Track previous positions to avoid oscillation
#         prev_move = None
        
#         while True:
#             client_sock, client_addr = s.accept()
#             print('New connection from', client_addr)
            
#             while True:
#                 data = client_sock.recv(1024)
#                 if data:
#                     try:
#                         # Parse game state
#                         yx1, yy1, yx2, yy2, rx1, ry1, rx2, ry2, ax, ay = literal_eval(data.decode())
                        
#                         # Wall avoidance - always highest priority
#                         if max(yx1, yx2) >= WIDTH - SEG_SIZE:
#                             move = "Left"
#                         elif min(yx1, yx2) <= SEG_SIZE:
#                             move = "Right"
#                         elif max(yy1, yy2) >= HEIGHT - SEG_SIZE:
#                             move = "Up"
#                         elif min(yy1, yy2) <= SEG_SIZE:
#                             move = "Down"
#                         else:
#                             # Check if we'll collide with red snake
#                             will_collide = False
                            
#                             # Calculate the direction to the apple
#                             x_diff = ax - yx1
#                             y_diff = ay - yy1
                            
#                             # Just like red snake, prefer X axis movement first
#                             if abs(x_diff) > 0:
#                                 move = "Right" if x_diff > 0 else "Left"
                                
#                                 # Check if this would cause collision
#                                 new_x = yx1 + (SEG_SIZE if move == "Right" else -SEG_SIZE)
#                                 if new_x == rx1 and yy1 == ry1:
#                                     will_collide = True
#                             else:
#                                 move = "Down" if y_diff > 0 else "Up"
                                
#                                 # Check if this would cause collision
#                                 new_y = yy1 + (SEG_SIZE if move == "Down" else -SEG_SIZE)
#                                 if yx1 == rx1 and new_y == ry1:
#                                     will_collide = True
                            
#                             # If collision detected, change direction (vertical/horizontal swap)
#                             if will_collide:
#                                 if move in ["Right", "Left"]:
#                                     move = "Down" if y_diff > 0 else "Up"
#                                     # Check if this alternative is safe
#                                     new_y = yy1 + (SEG_SIZE if move == "Down" else -SEG_SIZE)
#                                     if yx1 == rx1 and new_y == ry1:
#                                         # Neither horizontal nor vertical is safe, move away
#                                         move = "Up" if move == "Down" else "Down"
#                                 else:  # move in ["Up", "Down"]
#                                     move = "Right" if x_diff > 0 else "Left"
#                                     # Check if this alternative is safe
#                                     new_x = yx1 + (SEG_SIZE if move == "Right" else -SEG_SIZE)
#                                     if new_x == rx1 and yy1 == ry1:
#                                         # Neither vertical nor horizontal is safe, move away
#                                         move = "Left" if move == "Right" else "Right"
                            
#                             # Final wall check for the new move
#                             if move == "Right" and yx1 + SEG_SIZE >= WIDTH - SEG_SIZE:
#                                 move = "Left" if yx1 - SEG_SIZE > SEG_SIZE else "Up"
#                             elif move == "Left" and yx1 - SEG_SIZE <= SEG_SIZE:
#                                 move = "Right" if yx1 + SEG_SIZE < WIDTH - SEG_SIZE else "Up"
#                             elif move == "Down" and yy1 + SEG_SIZE >= HEIGHT - SEG_SIZE:
#                                 move = "Up" if yy1 - SEG_SIZE > SEG_SIZE else "Right"
#                             elif move == "Up" and yy1 - SEG_SIZE <= SEG_SIZE:
#                                 move = "Down" if yy1 + SEG_SIZE < HEIGHT - SEG_SIZE else "Right"
                                
#                         # Avoid oscillation
#                         if prev_move == "Right" and move == "Left":
#                             move = "Up" if yy1 - SEG_SIZE > SEG_SIZE else "Down"
#                         elif prev_move == "Left" and move == "Right":
#                             move = "Up" if yy1 - SEG_SIZE > SEG_SIZE else "Down"
#                         elif prev_move == "Up" and move == "Down":
#                             move = "Right" if yx1 + SEG_SIZE < WIDTH - SEG_SIZE else "Left"
#                         elif prev_move == "Down" and move == "Up":
#                             move = "Right" if yx1 + SEG_SIZE < WIDTH - SEG_SIZE else "Left"
                        
#                         prev_move = move
#                         client_sock.sendall(move.encode())
                        
#                     except Exception as e:
#                         print(f"Error processing data: {e}")
#                         client_sock.sendall("Straight".encode())
#                 else:
#                     break
                    
#             client_sock.close()

# if __name__ == "__main__":
#     handle_client()
# import socket
# from ast import literal_eval
# import random
# from collections import deque

# HOST = '0.0.0.0'  # Listen on all available interfaces
# PORT = 5001      # Port for yellow snake
# WIDTH = 800
# HEIGHT = 600
# SEG_SIZE = 20

# # Store recent positions to detect patterns
# last_positions = deque(maxlen=10)
# last_opponent_positions = deque(maxlen=10)

# def manhattan_distance(x1, y1, x2, y2):
#     """Calculate Manhattan distance between two points"""
#     return abs(x1 - x2) + abs(y1 - y2)

# def is_collision_danger(yx1, yy1, rx1, ry1, direction):
#     """Check if moving in a direction puts us at risk of collision"""
#     new_x, new_y = yx1, yy1
    
#     if direction == "Right":
#         new_x += SEG_SIZE
#     elif direction == "Left":
#         new_x -= SEG_SIZE
#     elif direction == "Down":
#         new_y += SEG_SIZE
#     elif direction == "Up":
#         new_y -= SEG_SIZE
    
#     # Check for immediate collision with opponent head
#     if new_x == rx1 and new_y == ry1:
#         return True
    
#     # Also check one step ahead for potential traps
#     opponent_direction = predict_opponent_direction(rx1, ry1)
#     if opponent_direction:
#         next_rx, next_ry = rx1, ry1
#         if opponent_direction == "Right":
#             next_rx += SEG_SIZE
#         elif opponent_direction == "Left":
#             next_rx -= SEG_SIZE
#         elif opponent_direction == "Down":
#             next_ry += SEG_SIZE
#         elif opponent_direction == "Up":
#             next_ry -= SEG_SIZE
            
#         # Check if we'd be in the opponent's next position
#         if new_x == next_rx and new_y == next_ry:
#             return True
    
#     return False

# def predict_opponent_direction(rx1, ry1):
#     """Try to predict opponent's next move based on recent positions"""
#     if len(last_opponent_positions) < 2:
#         return None
    
#     # Get last two positions
#     prev_rx, prev_ry = last_opponent_positions[-2]
    
#     # Calculate movement vector
#     dx = rx1 - prev_rx
#     dy = ry1 - prev_ry
    
#     if dx > 0:
#         return "Right"
#     elif dx < 0:
#         return "Left"
#     elif dy > 0:
#         return "Down"
#     elif dy < 0:
#         return "Up"
    
#     return None

# def get_safe_moves(yx1, yy1, rx1, ry1):
#     """Get all valid moves that don't hit walls or cause immediate collisions"""
#     possible_moves = []
    
#     # Check all four directions
#     if yx1 + SEG_SIZE < WIDTH - SEG_SIZE:
#         possible_moves.append("Right")
#     if yx1 - SEG_SIZE > SEG_SIZE:
#         possible_moves.append("Left")
#     if yy1 + SEG_SIZE < HEIGHT - SEG_SIZE:
#         possible_moves.append("Down")
#     if yy1 - SEG_SIZE > SEG_SIZE:
#         possible_moves.append("Up")
    
#     # Filter out dangerous moves
#     safe_moves = [m for m in possible_moves if not is_collision_danger(yx1, yy1, rx1, ry1, m)]
    
#     return safe_moves or possible_moves  # If no safe moves, return all possible moves

# def calculate_move_scores(yx1, yy1, rx1, ry1, ax, ay, moves):
#     """Score moves based on multiple factors"""
#     scores = []
    
#     for move in moves:
#         new_x, new_y = yx1, yy1
        
#         if move == "Right":
#             new_x += SEG_SIZE
#         elif move == "Left":
#             new_x -= SEG_SIZE
#         elif move == "Down":
#             new_y += SEG_SIZE
#         elif move == "Up":
#             new_y -= SEG_SIZE
        
#         # Calculate base score from apple distance (lower is better)
#         apple_dist = manhattan_distance(new_x, new_y, ax, ay)
#         score = 1000 - apple_dist  # Convert to a score where higher is better
        
#         # Add bonus for moves that increase distance from opponent
#         current_dist_to_opponent = manhattan_distance(yx1, yy1, rx1, ry1)
#         new_dist_to_opponent = manhattan_distance(new_x, new_y, rx1, ry1)
        
#         # If we're close to opponent, reward moves that increase distance
#         if current_dist_to_opponent < 5 * SEG_SIZE and new_dist_to_opponent > current_dist_to_opponent:
#             score += 50
        
#         # Avoid getting trapped against walls
#         wall_proximity = 0
#         if new_x <= 2 * SEG_SIZE or new_x >= WIDTH - 2 * SEG_SIZE:
#             wall_proximity += 1
#         if new_y <= 2 * SEG_SIZE or new_y >= HEIGHT - 2 * SEG_SIZE:
#             wall_proximity += 1
            
#         # Penalize moves that put us close to walls on two sides (corner situations)
#         if wall_proximity >= 2:
#             score -= 100
            
#         scores.append((move, score))
    
#     # Sort by score (descending)
#     scores.sort(key=lambda x: x[1], reverse=True)
#     return scores

# def handle_client():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen()
#         print(f"Yellow Snake Server listening on {HOST}:{PORT}")
        
#         while True:
#             client_sock, client_addr = s.accept()
#             print('New connection from', client_addr)
            
#             # Reset tracking for new game
#             last_positions.clear()
#             last_opponent_positions.clear()
            
#             while True:
#                 data = client_sock.recv(1024)
#                 if data:
#                     try:
#                         # Parse game state
#                         yx1, yy1, yx2, yy2, rx1, ry1, rx2, ry2, ax, ay = literal_eval(data.decode())
                        
#                         # Track positions
#                         last_positions.append((yx1, yy1))
#                         last_opponent_positions.append((rx1, ry1))
                        
#                         # Wall avoidance (absolute priority)
#                         if max(yx1, yx2) >= WIDTH - SEG_SIZE:
#                             move = "Left"
#                         elif min(yx1, yx2) <= SEG_SIZE:
#                             move = "Right"
#                         elif max(yy1, yy2) >= HEIGHT - SEG_SIZE:
#                             move = "Up"
#                         elif min(yy1, yy2) <= SEG_SIZE:
#                             move = "Down"
#                         else:
#                             # Get all safe moves
#                             safe_moves = get_safe_moves(yx1, yy1, rx1, ry1)
                            
#                             if not safe_moves:
#                                 # No safe moves, just try to avoid walls
#                                 if yx1 + SEG_SIZE < WIDTH - SEG_SIZE:
#                                     move = "Right"
#                                 elif yx1 - SEG_SIZE > SEG_SIZE:
#                                     move = "Left"
#                                 elif yy1 + SEG_SIZE < HEIGHT - SEG_SIZE:
#                                     move = "Down"
#                                 else:
#                                     move = "Up"
#                             else:
#                                 # Calculate scores for each move
#                                 scored_moves = calculate_move_scores(yx1, yy1, rx1, ry1, ax, ay, safe_moves)
                                
#                                 # Choose best move
#                                 move = scored_moves[0][0]
                                
#                                 # Add a small random element to be unpredictable (5% chance)
#                                 if random.random() < 0.05 and len(scored_moves) > 1:
#                                     move = random.choice(safe_moves)
                        
#                         client_sock.sendall(move.encode())
                        
#                     except Exception as e:
#                         print(f"Error processing data: {e}")
#                         client_sock.sendall("Straight".encode())
#                 else:
#                     break
                    
#             client_sock.close()

# if __name__ == "__main__":
#     handle_client()
# import socket
# from ast import literal_eval
# import random
# from collections import deque

# HOST = '0.0.0.0'  # Listen on all available interfaces
# PORT = 5001      # Port for yellow snake
# WIDTH = 800
# HEIGHT = 600
# SEG_SIZE = 20

# # Store recent positions to detect patterns
# last_positions = deque(maxlen=10)
# last_opponent_positions = deque(maxlen=10)

# def manhattan_distance(x1, y1, x2, y2):
#     """Calculate Manhattan distance between two points"""
#     return abs(x1 - x2) + abs(y1 - y2)

# def is_collision_danger(yx1, yy1, rx1, ry1, direction):
#     """Check if moving in a direction puts us at risk of collision"""
#     new_x, new_y = yx1, yy1
    
#     if direction == "Right":
#         new_x += SEG_SIZE
#     elif direction == "Left":
#         new_x -= SEG_SIZE
#     elif direction == "Down":
#         new_y += SEG_SIZE
#     elif direction == "Up":
#         new_y -= SEG_SIZE
    
#     # Check for immediate collision with opponent head
#     if new_x == rx1 and new_y == ry1:
#         return True
    
#     # Also check one step ahead for potential traps
#     opponent_direction = predict_opponent_direction(rx1, ry1)
#     if opponent_direction:
#         next_rx, next_ry = rx1, ry1
#         if opponent_direction == "Right":
#             next_rx += SEG_SIZE
#         elif opponent_direction == "Left":
#             next_rx -= SEG_SIZE
#         elif opponent_direction == "Down":
#             next_ry += SEG_SIZE
#         elif opponent_direction == "Up":
#             next_ry -= SEG_SIZE
            
#         # Check if we'd be in the opponent's next position
#         if new_x == next_rx and new_y == next_ry:
#             return True
    
#     return False

# def predict_opponent_direction(rx1, ry1):
#     """Try to predict opponent's next move based on recent positions"""
#     if len(last_opponent_positions) < 2:
#         return None
    
#     # Get last two positions
#     prev_rx, prev_ry = last_opponent_positions[-2]
    
#     # Calculate movement vector
#     dx = rx1 - prev_rx
#     dy = ry1 - prev_ry
    
#     if dx > 0:
#         return "Right"
#     elif dx < 0:
#         return "Left"
#     elif dy > 0:
#         return "Down"
#     elif dy < 0:
#         return "Up"
    
#     return None

# def get_safe_moves(yx1, yy1, rx1, ry1):
#     """Get all valid moves that don't hit walls or cause immediate collisions"""
#     possible_moves = []
    
#     # Check all four directions
#     if yx1 + SEG_SIZE < WIDTH - SEG_SIZE:
#         possible_moves.append("Right")
#     if yx1 - SEG_SIZE > SEG_SIZE:
#         possible_moves.append("Left")
#     if yy1 + SEG_SIZE < HEIGHT - SEG_SIZE:
#         possible_moves.append("Down")
#     if yy1 - SEG_SIZE > SEG_SIZE:
#         possible_moves.append("Up")
    
#     # Filter out dangerous moves
#     safe_moves = [m for m in possible_moves if not is_collision_danger(yx1, yy1, rx1, ry1, m)]
    
#     return safe_moves or possible_moves  # If no safe moves, return all possible moves

# def can_trap_opponent(yx1, yy1, rx1, ry1):
#     """Check if we can execute a trapping maneuver on the opponent"""
#     # Calculate what direction the opponent is moving
#     opponent_direction = predict_opponent_direction(rx1, ry1)
#     if not opponent_direction:
#         return None
    
#     # Check if we're in position to intercept opponent's path
#     dist = manhattan_distance(yx1, yy1, rx1, ry1)
    
#     # Only attempt trapping if we're close enough
#     if dist > 3 * SEG_SIZE:
#         return None
    
#     # Determine where the opponent will be in the next move
#     next_rx, next_ry = rx1, ry1
#     if opponent_direction == "Right":
#         next_rx += SEG_SIZE
#     elif opponent_direction == "Left":
#         next_rx -= SEG_SIZE
#     elif opponent_direction == "Down":
#         next_ry += SEG_SIZE
#     elif opponent_direction == "Up":
#         next_ry -= SEG_SIZE
    
#     # Check if we can move to intercept the opponent's path
#     possible_trap_moves = []
    
#     # Perpendicular interception (most effective trap)
#     if opponent_direction in ["Right", "Left"]:
#         # If opponent is moving horizontally, check if we can move vertically to intercept
#         if abs(yx1 - next_rx) <= SEG_SIZE and abs(yy1 - next_ry) == SEG_SIZE:
#             if yy1 < next_ry and yy1 + SEG_SIZE < HEIGHT - SEG_SIZE:
#                 possible_trap_moves.append("Down")
#             elif yy1 > next_ry and yy1 - SEG_SIZE > SEG_SIZE:
#                 possible_trap_moves.append("Up")
#     elif opponent_direction in ["Up", "Down"]:
#         # If opponent is moving vertically, check if we can move horizontally to intercept
#         if abs(yy1 - next_ry) <= SEG_SIZE and abs(yx1 - next_rx) == SEG_SIZE:
#             if yx1 < next_rx and yx1 + SEG_SIZE < WIDTH - SEG_SIZE:
#                 possible_trap_moves.append("Right")
#             elif yx1 > next_rx and yx1 - SEG_SIZE > SEG_SIZE:
#                 possible_trap_moves.append("Left")
    
#     # If we have multiple trap moves, choose one randomly to be unpredictable
#     if possible_trap_moves:
#         return random.choice(possible_trap_moves)
    
#     return None

# def calculate_move_scores(yx1, yy1, rx1, ry1, ax, ay, moves):
#     """Score moves based on multiple factors"""
#     scores = []
    
#     # First, check if we can execute a trapping maneuver
#     trap_move = can_trap_opponent(yx1, yy1, rx1, ry1)
#     if trap_move and trap_move in moves:
#         # If we can trap, strongly prefer that move
#         for move in moves:
#             if move == trap_move:
#                 # Give trapping an extremely high score to prioritize it
#                 scores.append((move, 10000))
#             else:
#                 # Calculate normal score for other moves
#                 new_x, new_y = yx1, yy1
                
#                 if move == "Right":
#                     new_x += SEG_SIZE
#                 elif move == "Left":
#                     new_x -= SEG_SIZE
#                 elif move == "Down":
#                     new_y += SEG_SIZE
#                 elif move == "Up":
#                     new_y -= SEG_SIZE
                
#                 # Calculate base score from apple distance
#                 apple_dist = manhattan_distance(new_x, new_y, ax, ay)
#                 score = 1000 - apple_dist
                
#                 # Handle other factors as usual
#                 current_dist_to_opponent = manhattan_distance(yx1, yy1, rx1, ry1)
#                 new_dist_to_opponent = manhattan_distance(new_x, new_y, rx1, ry1)
                
#                 if current_dist_to_opponent < 5 * SEG_SIZE and new_dist_to_opponent > current_dist_to_opponent:
#                     score += 50
                
#                 # Avoid wall traps
#                 wall_proximity = 0
#                 if new_x <= 2 * SEG_SIZE or new_x >= WIDTH - 2 * SEG_SIZE:
#                     wall_proximity += 1
#                 if new_y <= 2 * SEG_SIZE or new_y >= HEIGHT - 2 * SEG_SIZE:
#                     wall_proximity += 1
                    
#                 if wall_proximity >= 2:
#                     score -= 100
                    
#                 scores.append((move, score))
#     else:
#         # Normal scoring if no trap is possible
#         for move in moves:
#             new_x, new_y = yx1, yy1
            
#             if move == "Right":
#                 new_x += SEG_SIZE
#             elif move == "Left":
#                 new_x -= SEG_SIZE
#             elif move == "Down":
#                 new_y += SEG_SIZE
#             elif move == "Up":
#                 new_y -= SEG_SIZE
            
#             # Calculate base score from apple distance (lower is better)
#             apple_dist = manhattan_distance(new_x, new_y, ax, ay)
#             score = 1000 - apple_dist  # Convert to a score where higher is better
            
#             # Add bonus for moves that increase distance from opponent
#             current_dist_to_opponent = manhattan_distance(yx1, yy1, rx1, ry1)
#             new_dist_to_opponent = manhattan_distance(new_x, new_y, rx1, ry1)
            
#             # If we're close to opponent, reward moves that increase distance
#             if current_dist_to_opponent < 5 * SEG_SIZE and new_dist_to_opponent > current_dist_to_opponent:
#                 score += 50
            
#             # Avoid getting trapped against walls
#             wall_proximity = 0
#             if new_x <= 2 * SEG_SIZE or new_x >= WIDTH - 2 * SEG_SIZE:
#                 wall_proximity += 1
#             if new_y <= 2 * SEG_SIZE or new_y >= HEIGHT - 2 * SEG_SIZE:
#                 wall_proximity += 1
                
#             # Penalize moves that put us close to walls on two sides (corner situations)
#             if wall_proximity >= 2:
#                 score -= 100
                
#             scores.append((move, score))
    
#     # Sort by score (descending)
#     scores.sort(key=lambda x: x[1], reverse=True)
#     return scores

# def handle_client():
#     with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#         s.bind((HOST, PORT))
#         s.listen()
#         print(f"Yellow Snake Server listening on {HOST}:{PORT}")
        
#         while True:
#             client_sock, client_addr = s.accept()
#             print('New connection from', client_addr)
            
#             # Reset tracking for new game
#             last_positions.clear()
#             last_opponent_positions.clear()
            
#             while True:
#                 data = client_sock.recv(1024)
#                 if data:
#                     try:
#                         # Parse game state
#                         yx1, yy1, yx2, yy2, rx1, ry1, rx2, ry2, ax, ay = literal_eval(data.decode())
                        
#                         # Track positions
#                         last_positions.append((yx1, yy1))
#                         last_opponent_positions.append((rx1, ry1))
                        
#                         # Wall avoidance (absolute priority)
#                         if max(yx1, yx2) >= WIDTH - SEG_SIZE:
#                             move = "Left"
#                         elif min(yx1, yx2) <= SEG_SIZE:
#                             move = "Right"
#                         elif max(yy1, yy2) >= HEIGHT - SEG_SIZE:
#                             move = "Up"
#                         elif min(yy1, yy2) <= SEG_SIZE:
#                             move = "Down"
#                         else:
#                             # Get all safe moves
#                             safe_moves = get_safe_moves(yx1, yy1, rx1, ry1)
                            
#                             if not safe_moves:
#                                 # No safe moves, just try to avoid walls
#                                 if yx1 + SEG_SIZE < WIDTH - SEG_SIZE:
#                                     move = "Right"
#                                 elif yx1 - SEG_SIZE > SEG_SIZE:
#                                     move = "Left"
#                                 elif yy1 + SEG_SIZE < HEIGHT - SEG_SIZE:
#                                     move = "Down"
#                                 else:
#                                     move = "Up"
#                             else:
#                                 # Calculate scores for each move
#                                 scored_moves = calculate_move_scores(yx1, yy1, rx1, ry1, ax, ay, safe_moves)
                                
#                                 # Choose best move
#                                 move = scored_moves[0][0]
                                
#                                 # Add a small random element to be unpredictable (5% chance)
#                                 if random.random() < 0.05 and len(scored_moves) > 1:
#                                     move = random.choice(safe_moves)
                        
#                         client_sock.sendall(move.encode())
                        
#                     except Exception as e:
#                         print(f"Error processing data: {e}")
#                         client_sock.sendall("Straight".encode())
#                 else:
#                     break
                    
#             client_sock.close()

# if __name__ == "__main__":
#     handle_client()
import socket
from ast import literal_eval
import random
from collections import deque

HOST = '0.0.0.0'  # Listen on all available interfaces
PORT = 5001      # Port for yellow snake
WIDTH = 800
HEIGHT = 600
SEG_SIZE = 20

# Store recent positions to detect patterns
last_positions = deque(maxlen=10)
last_opponent_positions = deque(maxlen=10)

def manhattan_distance(x1, y1, x2, y2):
    """Calculate Manhattan distance between two points"""
    return abs(x1 - x2) + abs(y1 - y2)

def is_collision_danger(yx1, yy1, rx1, ry1, direction):
    """Check if moving in a direction puts us at risk of collision"""
    new_x, new_y = yx1, yy1
    
    if direction == "Right":
        new_x += SEG_SIZE
    elif direction == "Left":
        new_x -= SEG_SIZE
    elif direction == "Down":
        new_y += SEG_SIZE
    elif direction == "Up":
        new_y -= SEG_SIZE
    
    # Check for immediate collision with opponent head
    if new_x == rx1 and new_y == ry1:
        return True
    
    # Also check one step ahead for potential traps
    opponent_direction = predict_opponent_direction(rx1, ry1)
    if opponent_direction:
        next_rx, next_ry = rx1, ry1
        if opponent_direction == "Right":
            next_rx += SEG_SIZE
        elif opponent_direction == "Left":
            next_rx -= SEG_SIZE
        elif opponent_direction == "Down":
            next_ry += SEG_SIZE
        elif opponent_direction == "Up":
            next_ry -= SEG_SIZE
            
        # Check if we'd be in the opponent's next position
        if new_x == next_rx and new_y == next_ry:
            return True
    
    return False

def predict_opponent_direction(rx1, ry1):
    """Try to predict opponent's next move based on recent positions"""
    if len(last_opponent_positions) < 2:
        return None
    
    # Get last two positions
    prev_rx, prev_ry = last_opponent_positions[-2]
    
    # Calculate movement vector
    dx = rx1 - prev_rx
    dy = ry1 - prev_ry
    
    if dx > 0:
        return "Right"
    elif dx < 0:
        return "Left"
    elif dy > 0:
        return "Down"
    elif dy < 0:
        return "Up"
    
    return None

def get_safe_moves(yx1, yy1, rx1, ry1):
    """Get all valid moves that don't hit walls or cause immediate collisions"""
    possible_moves = []
    
    # Check all four directions
    if yx1 + SEG_SIZE < WIDTH - SEG_SIZE:
        possible_moves.append("Right")
    if yx1 - SEG_SIZE > SEG_SIZE:
        possible_moves.append("Left")
    if yy1 + SEG_SIZE < HEIGHT - SEG_SIZE:
        possible_moves.append("Down")
    if yy1 - SEG_SIZE > SEG_SIZE:
        possible_moves.append("Up")
    
    # Filter out dangerous moves
    safe_moves = [m for m in possible_moves if not is_collision_danger(yx1, yy1, rx1, ry1, m)]
    
    return safe_moves or possible_moves  # If no safe moves, return all possible moves

def can_trap_opponent(yx1, yy1, rx1, ry1):
    """Check if we can execute a trapping maneuver on the opponent"""
    # Calculate what direction the opponent is moving
    opponent_direction = predict_opponent_direction(rx1, ry1)
    if not opponent_direction:
        return None
    
    # Check if we're in position to intercept opponent's path
    dist = manhattan_distance(yx1, yy1, rx1, ry1)
    
    # Only attempt trapping if we're in the sweet spot - close enough to trap
    # but not too close to be dangerous
    if dist < 2 * SEG_SIZE or dist > 4 * SEG_SIZE:
        return None
    
    # Determine where the opponent will be in the next move
    next_rx, next_ry = rx1, ry1
    if opponent_direction == "Right":
        next_rx += SEG_SIZE
    elif opponent_direction == "Left":
        next_rx -= SEG_SIZE
    elif opponent_direction == "Down":
        next_ry += SEG_SIZE
    elif opponent_direction == "Up":
        next_ry -= SEG_SIZE
    
    # Check if we can move to intercept the opponent's path safely
    possible_trap_moves = []
    
    # Check wall proximity for safety
    is_near_wall = (
        rx1 <= 2 * SEG_SIZE or 
        rx1 >= WIDTH - 2 * SEG_SIZE or 
        ry1 <= 2 * SEG_SIZE or 
        ry1 >= HEIGHT - 2 * SEG_SIZE
    )
    
    # Don't attempt traps near walls (too risky)
    if is_near_wall:
        return None
    
    # Only try perpendicular interception (safer and more effective)
    if opponent_direction in ["Right", "Left"]:
        # If opponent is moving horizontally, check if we can move vertically to intercept
        if abs(yx1 - next_rx) <= SEG_SIZE and abs(yy1 - next_ry) == SEG_SIZE:
            if yy1 < next_ry and yy1 + SEG_SIZE < HEIGHT - 2 * SEG_SIZE:
                possible_trap_moves.append("Down")
            elif yy1 > next_ry and yy1 - SEG_SIZE > 2 * SEG_SIZE:
                possible_trap_moves.append("Up")
    elif opponent_direction in ["Up", "Down"]:
        # If opponent is moving vertically, check if we can move horizontally to intercept
        if abs(yy1 - next_ry) <= SEG_SIZE and abs(yx1 - next_rx) == SEG_SIZE:
            if yx1 < next_rx and yx1 + SEG_SIZE < WIDTH - 2 * SEG_SIZE:
                possible_trap_moves.append("Right")
            elif yx1 > next_rx and yx1 - SEG_SIZE > 2 * SEG_SIZE:
                possible_trap_moves.append("Left")
    
    # If we have possible trap moves, choose one (prefer the safest)
    if possible_trap_moves:
        return possible_trap_moves[0]  # Just take the first one for consistency
    
    return None

def calculate_move_scores(yx1, yy1, rx1, ry1, ax, ay, moves):
    """Score moves based on multiple factors"""
    scores = []
    
    # Calculate apple distance
    apple_dist = manhattan_distance(yx1, yy1, ax, ay)
    
    # Check if we can execute a trapping maneuver
    trap_move = can_trap_opponent(yx1, yy1, rx1, ry1)
    
    # Score all possible moves
    for move in moves:
        new_x, new_y = yx1, yy1
        
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
        current_dist_to_opponent = manhattan_distance(yx1, yy1, rx1, ry1)
        new_dist_to_opponent = manhattan_distance(new_x, new_y, rx1, ry1)
        
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
        print(f"Yellow Snake Server listening on {HOST}:{PORT}")
        
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
                        last_positions.append((yx1, yy1))
                        last_opponent_positions.append((rx1, ry1))
                        
                        # Wall avoidance (absolute priority)
                        if max(yx1, yx2) >= WIDTH - SEG_SIZE:
                            move = "Left"
                        elif min(yx1, yx2) <= SEG_SIZE:
                            move = "Right"
                        elif max(yy1, yy2) >= HEIGHT - SEG_SIZE:
                            move = "Up"
                        elif min(yy1, yy2) <= SEG_SIZE:
                            move = "Down"
                        else:
                            # Get all safe moves
                            safe_moves = get_safe_moves(yx1, yy1, rx1, ry1)
                            
                            if not safe_moves:
                                # No safe moves, just try to avoid walls
                                if yx1 + SEG_SIZE < WIDTH - SEG_SIZE:
                                    move = "Right"
                                elif yx1 - SEG_SIZE > SEG_SIZE:
                                    move = "Left"
                                elif yy1 + SEG_SIZE < HEIGHT - SEG_SIZE:
                                    move = "Down"
                                else:
                                    move = "Up"
                            else:
                                # Calculate scores for each move
                                scored_moves = calculate_move_scores(yx1, yy1, rx1, ry1, ax, ay, safe_moves)
                                
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
