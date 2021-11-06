import cv2

def get_image():
    org_img = cv2.imread('../images/ORGwall_and_paper.jpg')
    fea_img = cv2.imread('../images/PAGwall_and_paper.jpg')
    org_gray = cv2.cvtColor(org_img, cv2.COLOR_BGR2GRAY)
    fea_gray = cv2.cvtColor(fea_img, cv2.COLOR_BGR2GRAY)
    
    return org_img, fea_img, org_gray, fea_gray