"""Exceptions based on OAI-PMH v2.0 error codes.

The full list of error codes can be found in section 3.6 of The Open Archives 
Initiative Protocol for Metadata Harvesting specification, protocol version
2.0.

http://www.openarchives.org/OAI/openarchivesprotocol.html#ErrorConditions
"""

class ErrorBase(Exception):
    def oainame(self):
        name = self.__class__.__name__
        # strip off 'Error' part
        name = name[:-5]
        # lowercase error name
        name = name[0].lower() + name[1:]
        return name

class BadArgumentError(ErrorBase):
    """The request includes illegal arguments, is missing required arguments,
    includes a repeated argument, or values for arguments have an illegal
    syntax.
    """
    pass

class BadResumptionTokenError(ErrorBase):
    """The value of the resumptionToken argument is invalid or expired.
    """
    pass

class BadVerbError(ErrorBase):
    """Value of the verb argument is not a legal OAI-PMH verb, the verb
    argument is missing, or the verb argument is repeated.
    """
    pass


class CannotDisseminateFormatError(ErrorBase):
    """The metadata format identified by the value given for the metadataPrefix
    argument is not supported by the item or by the repository.
    """
    pass

class IdDoesNotExistError(ErrorBase):
    """The value of the identifier argument is unknown or illegal in this
    repository.
    """
    pass

class NoRecordsMatchError(ErrorBase):
    """The combination of the values of the from, until, set and metadataPrefix
    arguments results in an empty list.
    """
    pass

class NoMetadataFormatsError(ErrorBase):
    """There are no metadata formats available for the specified item.
    """
    pass

class NoSetHierarchyError(ErrorBase):
    """The repository does not support sets.
    """
    pass

class UnknownError(ErrorBase):
    """An unkown OAI-PMH error has occurred.
    """
    pass

# Errors not defined by OAI-PMH but which can occur in a client when the server
# is somehow misbehaving
class ClientError(Exception):
    def details(self):
        """Error details in human readable text.
        """
        raise NotImplementedError

class XMLSyntaxError(ClientError):
    """The OAI-PMH XML can not be parsed as it is not well-formed.
    """
    def details(self):
        return ("The data delivered by the server could not be parsed, as it "
                "is not well-formed XML.")
    
class DatestampError(ClientError):
    """The OAI-PMH datestamps were not proper UTC datestamps as by spec.
    """
    def __init__(self, datestamp):
        self.datestamp = datestamp

    def details(self):
        return ("An illegal datestamp was encountered: %s" % self.datestamp)
    
