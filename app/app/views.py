from django.shortcuts import render


def index(request):
    return render(request, 'index.html')



- name: Set up SSH connection
        env:
          CHECKFLOW_PEM: ${{ secrets.CHECKFLOW_PEM }}
        run: |
          mkdir -p ~/.ssh
          echo "${{ secrets.CHECKFLOW_PEM }}" > ~/.ssh/checkflow.pem
          chmod 600 ~/.ssh/checkflow.pem
          ssh-keyscan -H ec2-15-236-193-68.eu-west-3.compute.amazonaws.com >> ~/.ssh/known_hosts