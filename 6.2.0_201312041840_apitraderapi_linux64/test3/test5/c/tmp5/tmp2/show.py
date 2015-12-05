class BoostUnorderedMapPrinter:
    "prints a boost::unordered_map"
    
    class _iterator:
        def __init__ (self, fields):
            type_1 = fields.val.type.template_argument(0)
            type_2 = fields.val.type.template_argument(1)
            self.buckets = fields.val['table_']['buckets_']
            self.bucket_count = fields.val['table_']['bucket_count_']
            self.current_bucket = 0
            pair = "std::pair<%s const, %s>" % (type_1, type_2)
            self.pair_pointer = gdb.lookup_type(pair).pointer()
            self.base_pointer = gdb.lookup_type("boost::unordered_detail::value_base< %s >" % pair).pointer()
            self.node_pointer = gdb.lookup_type("boost::unordered_detail::hash_node<std::allocator< %s >, boost::unordered_detail::ungrouped>" % pair).pointer()
            self.node = self.buckets[self.current_bucket]['next_']

        def __iter__(self):
            return self

        def next(self):
            while not self.node:
                self.current_bucket = self.current_bucket + 1
                if self.current_bucket >= self.bucket_count:
                    raise StopIteration
                self.node = self.buckets[self.current_bucket]['next_']

            iterator = self.node.cast(self.node_pointer).cast(self.base_pointer).cast(self.pair_pointer).dereference()   
            self.node = self.node['next_']

            return ('%s' % iterator['first'], iterator['second'])

    def __init__(self, val):
        self.val = val
        print "fuckonback"

    def children(self):
        return self._iterator(self)

    def to_string(self):
        return "boost::unordered_map"
