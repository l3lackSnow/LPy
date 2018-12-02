import cv2

cv2.namedWindow('temp')
cv2.createTrackbar('bl', 'temp', 0, 255, 0)
cv2.createTrackbar('gl', 'temp', 0, 255, 0)
cv2.createTrackbar('rl', 'temp', 0, 255, 0)
cv2.createTrackbar('bh', 'temp', 255, 255, 0)
cv2.createTrackbar('gh', 'temp', 255, 255, 0)
cv2.createTrackbar('rh', 'temp', 255, 255, 0)

bl_temp=cv2.getTrackbarPos('bl', 'temp')
gl_temp=cv2.getTrackbarPos('gl', 'temp')
rl_temp=cv2.getTrackbarPos('rl', 'temp')

bh_temp=cv2.getTrackbarPos('bh', 'temp')
gh_temp=cv2.getTrackbarPos('gh', 'temp')
rh_temp=cv2.getTrackbarPos('rh', 'temp')
thresh=cv2.inRange(frame,(bl_temp,gl_temp,rl_temp),(bh_temp,gh_temp,rh_temp))