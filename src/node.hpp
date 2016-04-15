#pragma once
#include <bits/stdc++.h>
#include <stdio.h>
#include "message.hpp"
#include "simgrid/msg.h"
#include "xbt/log.h"
using namespace std;


// globals?

#define COMM_SIZE 10
#define COMP_SIZE 0
#define MAILBOX_NAME_SIZE 10

static int nb_bits = 24;
static int nb_keys = 0;
static int timeout = 50;
static int max_simulation_time = 1000;
static int periodic_stabilize_delay = 20;
static int periodic_fix_fingers_delay = 120;
static int periodic_check_predecessor_delay = 120;
static int periodic_lookup_delay = 10;

static const double sleep_delay = 4.9999;

extern long int smx_total_comms;

// a chord node
class Node {
  int id;                                 // my id
  string ip_prefix;
  string ip;                              // ip address for communication
  // char mailbox[MAILBOX_NAME_SIZE];        // my mailbox name (string representation of the id)
  vector<pair<int, string> > fingers;                    // finger table, of size nb_bits (fingers[0] is my successor)
  int pred_id;                            // predecessor id
  string pred_ip;   // predecessor's mailbox name
  int next_finger_to_fix;                 // index of the next finger to fix in fix_fingers()
  msg_comm_t comm_receive;                // current communication to receive
  double last_change_date;                // last time I changed a finger or my predecessor
public:
  Node(int id, string ip_prefix); // prefix is used for id2ip
  int join(int known_id);
  void leave();
  int find_successor(int id);
  int remote_find_successor(int ask_to_id, int id);
  int remote_get_predecessor(int ask_to_id);
  int closest_preceding_node(int id);
  void stabilize();
  void notify(int predecessor_candidate_id);
  void remote_notify(int notify_to, int predecessor_candidate_id);
  void fix_fingers();
  void check_predecessor();
  void random_lookup();
  void quit_notify();

  // new methods
  void single_iteration(); // run it's loop for one iteration. this uses simulator methods!

  // private
private:
  void handle_message(Message m);
  // convert ip to id and vice versa
  inline string id2ip(int id) {
    stringstream ss;
    ss << ip_prefix << id;
    string s;
    ss >> s;
    return s;
  }
  // use the prefix given through constructor.
  // global functions for sending/receiving messages with timeouts. will use the ismulator functions.
  // should probably add some kind of repeat?

  bool sendMessage(Message m, string ip);
  bool recvMessage(Message &m, string ip);
};