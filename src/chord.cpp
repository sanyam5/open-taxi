#include "simgrid/msg.h"
#include <bits/stdc++.h>
using namespace std;
XBT_LOG_NEW_DEFAULT_CATEGORY(example,"Messages specific for this msg example");
struct Message {
  int a, b;
  Message(int a, int b): a(a), b(b) {}
};
int alice(int argc, char **argv) {
  Message m(10, 20);
  msg_task_t task = MSG_task_create("my message", 0, 0, &m);
  MSG_task_send(task, "some address");
}

int bob(int argc, char **argv) {
  msg_task_t task;
  MSG_task_receive(&task, "some address");
  Message *m = static_cast<Message*>(MSG_task_get_data(task));
  XBT_INFO("got message... a= %d, b =%d", m->a, m->b);
}

int main(int argc, char *argv[])
{
  MSG_init(&argc, argv);
  msg_error_t res = MSG_OK;
  /* MSG_config("workstation/model","KCCFLN05"); */
  {                             /*  Simulation setting */
    MSG_create_environment(argv[1]);
  }
  {                             /*   Application deployment */
    MSG_function_register("alice", alice);
    MSG_function_register("bob", bob);
    MSG_launch_application(argv[2]);
  }
  res = MSG_main();
  XBT_INFO("Simulation time %g", MSG_get_clock());
  return 0;
}