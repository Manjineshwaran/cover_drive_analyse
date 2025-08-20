import numpy as np

def angle(a, b, c):
    """Return angle (in degrees) at b given 3 points (x,y)."""
    a, b, c = np.array(a), np.array(b), np.array(c)
    ba, bc = a - b, c - b
    cosang = np.dot(ba, bc) / (np.linalg.norm(ba) * np.linalg.norm(bc) + 1e-6)
    return np.degrees(np.arccos(np.clip(cosang, -1, 1)))

def distance(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))
