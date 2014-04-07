#
# Cookbook Name:: minecraft_class_server
# Recipe:: default
#
# Copyright 2013, YOUR_COMPANY_NAME
#
# All rights reserved - Do Not Redistribute
#

# To upload the cookbook, use:
# knife cookbook upload

# Update Apt
execute "apt-get update" do
	command "apt-get update"
end

# Install Apache
package "apache2" do
	action :install
end

service "apache2" do
	action [ :enable, :start ]
end

cookbook_file "/var/www/index.html" do
  action :create
	source "index.html"
	mode "0644"
end

# Install Java


# Install Git
package "git" do
	action :install
end

# Setup a user
user "minecraft" do
  action :create
  supports :manage_home => true
  comment "A minecraft administrator wahoo"
  uid 1234
  gid "users"
  home "/home/minecraft"
  shell "/bin/bash"
  # mine1234 is the pass
  password "$1$WARHpU5L$g4xv7tHDqvmGKVSdDx0zb1"
end

# Add the user to SUDO group
group "sudo" do
  action :modify
  members "minecraft"
  append true
end