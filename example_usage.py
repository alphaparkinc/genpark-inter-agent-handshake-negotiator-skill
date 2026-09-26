import sys
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from client import InterAgentHandshakeNegotiatorClient

def main():
    client = InterAgentHandshakeNegotiatorClient()
    res = client.negotiate_handshake()
    print("=== Inter-Agent Handshake Negotiator Output ===")
    print(f"Initiator: {res['initiator_agent_id']} <-> Peer: {res['peer_agent_id']}")
    print(f"Handshake Established: {res['handshake_established']} (Score: {res['compatibility_score']})")
    print(f"Status Directive: {res['status_directive']}")
    print("\nNegotiated Session Parameters:")
    for k, v in res['negotiated_parameters'].items():
        print(f"  * {k:25s}: {v}")

if __name__ == '__main__':
    main()
