#include "node.hpp"
Node::Node(int id, string ip_prefix): id(id), ip_prefix(ip_prefix), ip(id2ip(id)) {

}
  // int join(int known_id);
  // void leave();
  // int find_successor(int id);
  // int remote_find_successor(int ask_to_id, int id);
  // int remote_get_predecessor(int ask_to_id);
  // int closest_preceding_node(int id);
  // void stabilize();
  // void notify(int predecessor_candidate_id);
  // void remote_notify(int notify_to, int predecessor_candidate_id);
  // void fix_fingers();
  // void check_predecessor();
  // void random_lookup();
  // void quit_notify();