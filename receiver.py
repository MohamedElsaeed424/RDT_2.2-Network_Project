class ReceiverProcess:
    """ Represent the receiver process in the application layer  """
    __buffer = list()

    @staticmethod
    def deliver_data(data):
        """ deliver data from the transport layer RDT receiver to the application layer
        :param data: a character received by the RDT RDT receiver
        :return: no return value
        """
        ReceiverProcess.__buffer.append(data)
        return

    @staticmethod
    def get_buffer():
        """ To get the message the process received over the network
        :return:  a python list of characters represent the incoming message
        """
        return ReceiverProcess.__buffer


class RDTReceiver:
    """" Implement the Reliable Data Transfer Protocol V2.2 Receiver Side """

    def __init__(self):
        self.sequence = '0'

    def get_sequence(self):
        return self.sequence

    @staticmethod
    def is_corrupted(packet, self):
        """ Check if the received packet from sender is corrupted or not
            :param packet: a python dictionary represent a packet received from the sender
            :return: True -> if the reply is corrupted | False ->  if the reply is NOT corrupted
        """
        # TODO provide your own implementation
        return (RDTReceiver.get_sequence(self) != packet['sequence_number']
                or packet['checksum'] != ord(RDTReceiver.get_sequence(self)))
        pass

    @staticmethod
    def is_expected_seq(rcv_pkt, exp_seq):
        """ Check if the received reply from receiver has the expected sequence number
         :param rcv_pkt: a python dictionary represent a packet received by the receiver
         :param exp_seq: the receiver expected sequence number '0' or '1' represented as a character
         :return: True -> if ack in the reply match the   expected sequence number otherwise False
        """
        # TODO provide your own implementation
        return rcv_pkt['sequence_number'] == exp_seq
        pass

    @staticmethod
    def make_reply_pkt(seq, checksum):
        """ Create a reply (feedback) packet with to acknowledge the received packet
        :param seq: the sequence number '0' or '1' to be acknowledged
        :param checksum: the checksum of the ack the receiver will send to the sender
        :return:  a python dictionary represent a reply (acknowledgement)  packet
        """
        reply_pck = {
            'ack': seq,
            'checksum': checksum
        }
        return reply_pck

    def rdt_rcv(self, rcv_pkt):
        """  Implement the RDT v2.2 for the receiver
        :param rcv_pkt: a packet delivered by the network layer 'udt_send()' to the receiver
        :return: the reply packet
        """
        # TODO provide your own implementation
        if self.is_corrupted(rcv_pkt, self):
            rec_seq_num = rcv_pkt['sequence_number']
            #print(ord(rec_seq_num) , rec_seq_num)
            new_seq_num = ' '
            if ord(rec_seq_num) == 49:  # if 1 change to 0
                new_seq_num = '0'
            else:
                new_seq_num = '1'

        reply_pkt = self.make_reply_pkt(new_seq_num, ord(new_seq_num))

        if not self.is_expected_seq(reply_pkt , rcv_pkt['sequence_number']):



        # deliver the data to the process in the application layer
        ReceiverProcess.deliver_data(rcv_pkt['data'])

        return reply_pkt

        return None
