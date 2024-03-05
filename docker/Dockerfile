FROM osrf/ros:noetic-desktop-full

RUN apt-get update
RUN apt-get install -y git && apt-get install -y python3-pip


RUN git clone https://github.com/QuentinDervin/ros-tutorial-repo.git

RUN echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
RUN echo "source /ros-tutorial-repo/bin_copy/turtlebash.sh" >> ~/.bashrc
RUN echo "source /ros-tutorial-repo/bin_copy/dockerbash.sh" >> ~/.bashrc

RUN echo "source /ros-tutorial-repo/devel/setup.bash" >> ~/.bashrc

RUN /bin/bash -c 'source /opt/ros/noetic/setup.bash; cd ros-tutorial-repo/; catkin_make'

#Only worked when relevant to commands, does not effect bash terminals once container launched
#RUN /bin/bash -c 'source /ros-tutorial-repo/bin_copy/turtlebash.sh'
#RUN /bin/bash -c 'source /opt/ros/noetic/setup.bash'

#COPY entrypoint.sh /entrypoint.sh
#RUN chmod +x /entrypoint.sh
#ENTRYPOINT [ "/entrypoint.sh" ]

