#!/usr/bin/env python3

import docker
import sys

def container_exists(client, container_name):
    try:
        client.containers.get(container_name)
        return True
    except docker.errors.NotFound:
        return False

def get_container_status(client, container_name):
    if container_exists(client, container_name):
        container = client.containers.get(container_name)
        return container.status
    else:
        return "Container not found"

def start_container(client, container_name):
    if container_exists(client, container_name):
        container = client.containers.get(container_name)
        container.start()
        return "Container started"
    else:
        return "Container not found"

def stop_container(client, container_name):
    if container_exists(client, container_name):
        container = client.containers.get(container_name)
        container.stop()
        return "Container stopped"
    else:
        return "Container not found"

if __name__ == "__main__":
    client = docker.from_env()
    container_name = "my-container"

    if len(sys.argv) != 2:
        print("Usage: python manage_container.py [status/start/stop]")
        sys.exit(1)

    action = sys.argv[1]

    if action == "status":
        print(get_container_status(client, container_name))
    elif action == "start":
        print(start_container(client, container_name))
    elif action == "stop":
        print(stop_container(client, container_name))
    else:
        print("Invalid action. Use 'status', 'start', or 'stop'.")
        sys.exit(1)
