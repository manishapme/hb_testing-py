import unittest

import party


class PartyTests(unittest.TestCase):
    """Tests for my party site."""

    def setUp(self):
        self.client = party.app.test_client()
        party.app.config['TESTING'] = True

    def test_homepage(self):
        result = self.client.get("/")
        self.assertIn("I'm having a party", result.data)

    def test_no_rsvp_yet(self):
        result = self.client.get("/")
        # Add a test to show we haven't RSVP'd yet
        self.assertIn("Please RSVP", result.data)
        # test that you don't see the party details
        self.assertNotIn("Party Details", result.data)

    def test_rsvp(self):
        result = self.client.post("/rsvp",
                                  data={'name': "Jane", 'email': "jane@jane.com"},
                                  follow_redirects=True)
        # check that once we log in we see party details--but not the form!
        self.assertNotIn("Please RSVP", result.data)
        self.assertIn("Party Details", result.data)

    def test_rsvp_mel(self):
        result = self.client.post("/rsvp",
                                   data={"name": "Mel Melitpolski", "email": "mel@ubermelon"},
                                   follow_redirects=True)
        # write a test that mel can't invite himself
        self.assertIn("Sorry, Mel.", result.data)



if __name__ == "__main__":
    unittest.main()