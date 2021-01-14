#!/usr/bin/env python
import tf
import rospy

if __name__ == '__main__':

  rospy.init_node('simplem_tf_br')

  blaser_blink = tf.TransformBroadcaster()
  blink_bfprint = tf.TransformBroadcaster()
  base_blink = tf.TransformBroadcaster()

  rate = rospy.Rate(100)

  while not rospy.is_shutdown():

    blink_bfprint.sendTransform((0, 0, 0.062),
        tf.transformations.quaternion_from_euler(0, 0, 0),
        rospy.Time.now(),"base_link","base_footprint")

    base_blink.sendTransform((0, 0, 0.0),
        tf.transformations.quaternion_from_euler(0, 0, 0),
        rospy.Time.now(),"base","base_link")

    blaser_blink.sendTransform((0, 0, 0.045),
        tf.transformations.quaternion_from_euler(0, 0, 0),
        rospy.Time.now(),"base_scan","base_link")

    rate.sleep()
